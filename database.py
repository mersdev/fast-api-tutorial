from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

# Step 1: Create Database engine
engine = create_engine(os.getenv("DATABASE_URL"))

# configures the session to be used for database operations
# autocommit & autoflush = False - More Control Over Transaction
SessionLocal = sessionmaker(autocommit = False, autoflush= False, bind = engine)

# serves as the base class for declarative models 
Base = declarative_base()

