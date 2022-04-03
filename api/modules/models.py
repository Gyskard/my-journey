from sqlalchemy import Column, Date, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.types import ARRAY
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Location(Base):
    __tablename__ = 'location'

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String)
    house_number_street = Column(Integer)
    street_name = Column(String)
    city = Column(String)
    country = Column(String)
    postal_code = Column(Integer)


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True, unique=True)
    first_name = Column(String)
    last_name = Column(String)

    events = relationship('Event', secondary='participation', back_populates='persons')


class Event(Base):
    __tablename__ = 'event'

    id = Column(Integer, primary_key=True, unique=True)
    event_name = Column(String)
    description = Column(String)
    date = Column(Date)
    pictures = Column(ARRAY(String))
    location_id = Column(ForeignKey('location.id'))

    location = relationship('Location', lazy='joined')
    persons = relationship('Person', secondary='participation', back_populates='events', lazy='joined')


class Participation(Base):
    __tablename__ = 'participation'
    __table_args__ = (
        UniqueConstraint('event_id', 'person_id', name='person_in_event'),
    )

    event_id = Column(Integer, ForeignKey('event.id'), primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'), primary_key=True)
