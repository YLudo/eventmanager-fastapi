from sqlalchemy.orm import Session
from app.schemas.event import EventCreate
from app.utils.geocoding import get_coordinates_from_location
from app.utils.email import send_event_confirmation
from app.crud import event as crud_event
from app.models.user import User

async def create_event_with_side_effects(event_data: EventCreate, db: Session, user: User):
    coords = await get_coordinates_from_location(event_data.location)

    db_event = crud_event.create_event(db, event_data, user_id=user.id)
    db_event.coordinates = coords
    db.commit()
    db.refresh(db_event)

    send_event_confirmation(user.email, event_data.title)
    return db_event
