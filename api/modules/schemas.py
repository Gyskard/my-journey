from datetime import date

from pydantic import BaseModel


class Location(BaseModel):
    house_number_street: int
    street_name: str
    city: str
    county: str
    postal_code: int


class LocationResponse(Location):
    id: int

    class Config:
        orm_mode = True


class Person(BaseModel):
    first_name: str
    last_name: str


class PersonResponse(Person):
    id: int

    class Config:
        orm_mode = True


class Event(BaseModel):
    description: str
    date: date
    location_id: int


class EventResponse(Event):
    id: int

    class Config:
        orm_mode = True


class Participation(BaseModel):
    event_id: int
    person_id: int
