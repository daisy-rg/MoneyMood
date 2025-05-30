from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from datetime import date
from models import User, Income, Transactions, Base

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


    income = Income(
        amount=round(fake.random_number(digits=5) / 100, 2),  
        source=fake.company(),
        user=user
    )


    transaction = Transactions(
        amount=round(fake.random_number(digits=4) / 100, 2), 
        date= fake.date_between(start_date='-1y', end_date='today'),
        category=fake.word(),
        description=fake.sentence(),
        user=user 
    )


    users.append(user)

session.add_all(users)
session.commit()    