from fastapi import FastAPI
from app.db.database import engine, Base
from app.api import user, event

app = FastAPI(title="Event Manager API")

Base.metadata.create_all(bind=engine)

app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(event.router, prefix="/events", tags=["Events"])