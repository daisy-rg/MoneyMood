from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from models import Team, Coach, Base

engine = create_engine('sqlite:///fuata_dimba.db')
Session = sessionmaker(bind=engine)
session = Session()

# Creating a faker instance
fake = Faker()