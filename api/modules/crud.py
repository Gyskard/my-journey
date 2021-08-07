from sqlalchemy.orm import Session

from . import models, schemas


def create_location(db: Session, location: schemas.Location):
    db_location = models.Location(
        house_number_street=location.house_number_street,
        street_name=location.street_name,
        city=location.city,
        county=location.county,
        postal_code=location.postal_code
    )
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location


def get_location_by_all_infos(db: Session, location: schemas.Location):
    return db.query(models.Location).filter(models.Location.city == location.city) \
        .filter(models.Location.county == location.county) \
        .filter(models.Location.postal_code == location.postal_code) \
        .filter(models.Location.street_name == location.street_name) \
        .filter(models.Location.house_number_street == location.house_number_street) \
        .first()


def get_location_by_id(db: Session, location_id: int):
    return db.query(models.Location).filter(models.Location.id == location_id).first()


def delete_location_by_id(db: Session, location_id: int):
    db_location = db.query(models.Location).filter(models.Location.id == location_id).first()
    db.delete(db_location)
    db.commit()
    return True


def create_person(db: Session, person: schemas.Person):
    db_person = models.Person(
        first_name=person.first_name,
        last_name=person.last_name
    )
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person


def get_person_by_all_infos(db: Session, person: schemas.Person):
    return db.query(models.Person).filter(models.Person.first_name == person.first_name) \
        .filter(models.Person.last_name == person.last_name) \
        .first()


def get_person_by_id(db: Session, person_id: int):
    return db.query(models.Person).filter(models.Person.id == person_id).first()


def delete_person_by_id(db: Session, person_id: int):
    db_person = db.query(models.Person).filter(models.Person.id == person_id).first()
    db.delete(db_person)
    db.commit()
    return True


def create_event(db: Session, event: schemas.Event):
    db_event = models.Event(
        description=event.description,
        date=event.date,
        location_id=event.location_id
    )
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


def create_participation(db: Session, participation: schemas.Participation):
    db_participation = models.Participation(
        event_id=participation.event_id,
        person_id=participation.person_id
    )
    db.add(db_participation)
    db.commit()
    db.refresh(db_participation)
    return db_participation
