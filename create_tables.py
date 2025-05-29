from app.db.database import Base, engine
from app.models.user import User
from app.models.event import Event

print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("✅ Tables created.")