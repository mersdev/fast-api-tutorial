from app.database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, ForeignKey, text
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key= True, nullable=False)
    username = Column(String(50), unique=True)
    password = Column(String)
    posts = relationship("Post", back_populates = "user")
    
class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key= True, index=True)
    title = Column(String(50))
    content = Column(String(100))
    user_id = Column(Integer, ForeignKey("users.id") )
    published = Column(Boolean, server_default='TRUE')
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    user = relationship("User", back_populates = "posts")