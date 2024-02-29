from pydantic import BaseModel, validator
from datetime import datetime

class PostBase(BaseModel):
    title: str
    content: str | None

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    user_id: int
    created_at: datetime
    
    @validator("created_at", pre=True)
    def created_format(cls, value: datetime) -> str:
        return value.strftime("%Y-%m-%d %H:%M")
    
    class Config:
        orm_mode = True
        
class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str
    
class User(UserBase):
    id: int
    posts: list[Post] = []

    class Config:
        orm_mode = True