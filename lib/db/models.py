from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'  

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    profession = Column(String)


class Income(Base):
    __tablename__ = 'income'

    id = Column(Integer, primary_key=True)
    amount = Column (float , nullable=False)
    source = =Column (String)



class Transactions(Base):
     __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    amount = Column (float , nullable=False)
    date = Column(date)
    category = Column(String nullable=False)
    description = Column (String())




engine = create_engine('sqlite:///finance.db')
Base.metadata.create_all(engine)
