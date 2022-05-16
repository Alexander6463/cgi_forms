from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, Float, String, create_engine

Base = declarative_base()
engine = create_engine('sqlite:///my_db.db', echo=True)
SessionLocal = sessionmaker(bind=engine)


class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    mass = Column(Float)
    galaxy = Column(String)


class Galaxy(Base):
    __tablename__ = 'galaxy'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


class Spaceship(Base):
    __tablename__ = 'spaceship'
    id = Column(Integer, primary_key=True)
    cost = Column(Float)
    mass = Column(Float)
    producer = Column(String)
