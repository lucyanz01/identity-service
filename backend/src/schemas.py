from pydantic import EmailStr, Field, BaseModel
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=8)

class UserLogin(BaseModel):
    email: EmailStr
    password: str 

class UserOut(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime

    class Config: 
        from_attributes = True 