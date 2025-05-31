from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, create_engine
from sqlalchemy.orm import relationship, declarative_base
from datetime import date
from enum import Enum

Base = declarative_base()

class TransactionCategory(Enum):
    FOOD = "Food"
    RENT = "Rent"
    FEES = "Fees"
    OTHER = "Other"


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    profession = Column(String)
    
    income = relationship("Income", back_populates="user", cascade="all, delete-orphan")
    transactions = relationship("Transactions", back_populates="user", cascade="all, delete-orphan")

   
   

class Income(Base):
    __tablename__ = 'income'

    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    source = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    user = relationship("User", back_populates="income")

class Transactions(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    date = Column(Date)
    category = Column(String, nullable=False)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    user = relationship("User", back_populates="transactions") 

engine = create_engine('sqlite:///finance.db')
Base.metadata.create_all(engine)
