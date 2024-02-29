from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://xdman:1234@localhost:5432/blog"

# Step 1: Create Database engine
engine = create_engine(DATABASE_URL)

# configures the session to be used for database operations
# autocommit & autoflush = False - More Control Over Transaction
SessionLocal = sessionmaker(autocommit = False, autoflush= False, bind = engine)

# serves as the base class for declarative models 
Base = declarative_base()

