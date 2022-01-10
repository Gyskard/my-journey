from datetime import date
from typing import Optional
from pydantic import BaseModel


class Location(BaseModel):
    name: str
    house_number_street: Optional[int] = None
    street_name: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    postal_code: Optional[int] = None


class LocationResponse(Location):
    id: int

    class Config:
        orm_mode = True


class Person(BaseModel):
    first_name: str
    last_name: Optional[str] = None


class PersonResponse(Person):
    id: int

    class Config:
        orm_mode = True


class Event(BaseModel):
    event_name: str
    description: Optional[str] = None
    date: date
    location_id: int


class EventResponse(Event):
    id: int

    class Config:
        orm_mode = True


class Participation(BaseModel):
    event_id: int
    person_id: int
