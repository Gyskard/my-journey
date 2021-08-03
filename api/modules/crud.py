from sqlalchemy.orm import Session

from . import models, schemas


def create_location(db: Session, location: schemas.Location):
    db_location = models.Location(
        house_number_street=location.house_number_street,
        street_name=location.street_name,
        city=location.city,
        county=location.county,
        postal_code=location.postal_code)
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location
