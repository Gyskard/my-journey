from sqlalchemy import Column, Date, ForeignKey, Integer, String, Table, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Location(Base):
    __tablename__ = 'location'

    id = Column(Integer, primary_key=True, unique=True, server_default=text("nextval('location_id_seq'::regclass)"))
    house_number_street = Column(Integer)
    street_name = Column(String)
    city = Column(String)
    county = Column(String)
    postal_code = Column(Integer)


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True, unique=True, server_default=text("nextval('person_id_seq'::regclass)"))
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)


class Note(Base):
    __tablename__ = 'note'

    id = Column(Integer, primary_key=True, unique=True, server_default=text("nextval('notes_id_seq'::regclass)"))
    description = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    location_id = Column(ForeignKey('location.id'), nullable=False)

    location = relationship('Location')
    persons = relationship('Person', secondary='participation')


t_participation = Table(
    'participation', metadata,
    Column('note_id', ForeignKey('note.id')),
    Column('person_id', ForeignKey('person.id'))
)
