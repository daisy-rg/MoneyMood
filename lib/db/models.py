from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, create_engine
from sqlalchemy.orm import relationship, declarative_base
from datetime import date

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    profession = Column(String)

    incomes = relationship('Income', backref='user')
    transactions = relationship('Transactions', backref='user')

class Income(Base):
    __tablename__ = 'income'

    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    source = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

class Transactions(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    date = Column(Date)
    category = Column(String, nullable=False)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))


engine = create_engine('sqlite:///finance.db')
Base.metadata.create_all(engine)
