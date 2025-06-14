from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.db.dependency import get_db
from app.schemas.event import EventCreate, EventUpdate, EventOut
from app.core.deps import get_current_user
from app.models.user import User
from app.crud import event as crud_event
from app.services.event_service import create_event_with_side_effects
from app.utils.cache import cache

router = APIRouter()

@router.get("/", response_model=List[EventOut])
def read_events(db: Session = Depends(get_db)):
    cached = cache.get("events")
    if cached is not None:
        return cached
    events = crud_event.get_events(db)
    cache.set("events", events)
    return events

@router.get("/{event_id}", response_model=EventOut)
def read_event(event_id: int, db: Session = Depends(get_db)):
    cache_key = f"event:{event_id}"
    cached = cache.get(cache_key)
    if cached is not None:
        return cached
    event = crud_event.get_event(db, event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    cache.set(cache_key, event)
    return event

@router.post("/", response_model=EventOut)
async def create_event(event: EventCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_event = await create_event_with_side_effects(event, db, current_user)
    cache.invalidate("events")
    cache.invalidate(f"event:{db_event.id}")
    return db_event

@router.put("/{event_id}", response_model=EventOut)
def update_event(event_id: int, updated_event: EventUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    existing = crud_event.get_event(db, event_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Event not found")
    if existing.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not allowed to update this event")
    updated = crud_event.update_event(db, event_id, updated_event)
    cache.invalidate("events")
    cache.invalidate(f"event:{event_id}")
    return updated

@router.delete("/{event_id}")
def delete_event(event_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    existing = crud_event.get_event(db, event_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Event not found")
    if existing.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not allowed to delete this event")
    crud_event.delete_event(db, event_id)
    cache.invalidate("events")
    cache.invalidate(f"event:{event_id}")
    return {"message": "Event deleted"}
