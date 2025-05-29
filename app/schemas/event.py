from pydantic import BaseModel, Field
from datetime import datetime

class EventBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=100, description="Titre de l'événement")
    description: str = Field(..., max_length=500, description="Description de l'événement")
    location: str = Field(..., min_length=2, description="Ville ou lieu de l'événement")
    date: datetime = Field(..., description="Date et heure de l'événement (format ISO 8601)")

class EventCreate(EventBase):
    pass

class EventUpdate(EventBase):
    pass

class EventOut(EventBase):
    id: int
    owner_id: int
    coordinates: str | None = None

    class Config:
        orm_mode = True
