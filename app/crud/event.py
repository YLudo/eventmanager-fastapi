from sqlalchemy.orm import Session
from app.models.event import Event
from app.schemas.event import EventCreate, EventUpdate

def get_events(db: Session):
    return db.query(Event).all()

def get_event(db: Session, event_id: int):
    return db.query(Event).filter(Event.id == event_id).first()

def create_event(db: Session, event: EventCreate, user_id: int):
    db_event = Event(**event.dict(), owner_id=user_id)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

def update_event(db: Session, event_id: int, event_data: EventUpdate):
    event = db.query(Event).filter(Event.id == event_id).first()
    if event:
        for key, value in event_data.dict().items():
            setattr(event, key, value)
        db.commit()
        db.refresh(event)
    return event

def delete_event(db: Session, event_id: int):
    event = db.query(Event).filter(Event.id == event_id).first()
    if event:
        db.delete(event)
        db.commit()
    return event
