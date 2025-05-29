from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    email: EmailStr = Field(..., description="Adresse email de l'utilisateur")
    password: str = Field(..., min_length=6, max_length=100, description="Mot de passe (min 6 caractères)")
    full_name: str = Field(default="", max_length=100, description="Nom complet de l'utilisateur")

class UserOut(BaseModel):
    id: int
    email: EmailStr
    full_name: str
    is_active: bool
    is_admin: bool

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str
