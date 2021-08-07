from sqlalchemy import Column, Date, ForeignKey, Integer, String, Table, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Location(Base):
    __tablename__ = 'location'

    id = Column(Integer, primary_key=True, unique=True)
    house_number_street = Column(Integer)
    street_name = Column(String)
    city = Column(String)
    county = Column(String)
    postal_code = Column(Integer)


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True, unique=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)


class Event(Base):
    __tablename__ = 'event'

    id = Column(Integer, primary_key=True, unique=True)
    description = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    location_id = Column(ForeignKey('location.id'), nullable=False)

    location = relationship('Location')
    persons = relationship('Person', secondary='participation')


t_participation = Table(
    'participation', metadata,
    Column('event_id', ForeignKey('event.id'), nullable=False),
    Column('person_id', ForeignKey('person.id'), nullable=False)
)
