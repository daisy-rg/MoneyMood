from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from models import User, Base

engine = create_engine('sqlite:///finance.db')
Session = sessionmaker(bind=engine)
session = Session()

# Creating a faker instance
fake = Faker()

users = []

for i in range (30):
    #creating a user
    user = User(
        name=fake.name(),
        age=fake.random_int(min=18, max=65),
        profession=fake.job(), 
    )
    users.append(user)

session.add_all(users)
session.commit()    