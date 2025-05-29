from sqlalchemy import  Column, Integer, String, MetaData, Table, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base= declarative_base(metadata=metadata)