from datetime import date
from typing import Optional, List
from pydantic import BaseModel, validator


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


class ParticipationRequest(BaseModel):
    event_id: int
    person_id_list: List[int]


class Filter(BaseModel):
    search: Optional[str] = None
    date: Optional[str] = None
    order_by: str

    @validator('order_by')
    def order_by_must_have_valid_value(cls, v):
        if v not in ["ascending", "descending"]:
            raise ValueError('must have ascending or descending value')
        return v
