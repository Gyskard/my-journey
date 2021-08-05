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
