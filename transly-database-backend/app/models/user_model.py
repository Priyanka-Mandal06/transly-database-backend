from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# Request model for Register API
class RegisterUser(BaseModel):
    username: str
    email: EmailStr
    password: str

# Request model for Login API
class LoginUser(BaseModel):
    email: EmailStr
    password: str

# Internal DB model for User
class UserInDB(BaseModel):
    id: Optional[str] = None
    username: str
    email: EmailStr
    password: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

# Response model (safe)
class UserResponse(BaseModel):
    id: str
    username: str
    email: EmailStr
    created_at: datetime
