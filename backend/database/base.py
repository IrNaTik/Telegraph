from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine("sqlite:///main.db")
metadata = MetaData()

# Такой подход вместо with session() только лишь для удобства читаемости
session = sessionmaker(bind=engine)
current_session = scoped_session(session) # Фабрика сессий

@as_declarative(metadata=metadata)
class Base:
    pass