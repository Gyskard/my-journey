from sqlalchemy.orm import Session

from . import models, schemas


def create_location(db: Session, location: schemas.Location):
    db_location = models.Location(
        name=location.name,
        house_number_street=location.house_number_street,
        street_name=location.street_name,
        city=location.city,
        country=location.country,
        postal_code=location.postal_code
    )
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location


def get_location_by_all_infos(db: Session, location: schemas.Location):
    return db.query(models.Location) \
        .filter(models.Location.name == location.name) \
        .filter(models.Location.city == location.city) \
        .filter(models.Location.country == location.country) \
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
    return db.query(models.Person) \
        .filter(models.Person.first_name == person.first_name) \
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


def get_event(db: Session, event_id: int):
    return db.query(models.Event).filter(models.Event.id == event_id).first()


def get_person_by_event(db: Session, event_id: int):
    db_person_event = []
    db_participation = db.query(models.Participation.person_id).filter(models.Participation.event_id == event_id).all()
    for event in db_participation:
        db_person_event.append(event.person_id)
    return db_person_event


def get_event_by_person(db: Session, person_id: int):
    db_event_person = []
    db_participation = db.query(models.Participation.event_id).filter(models.Participation.person_id == person_id).all()
    for person in db_participation:
        db_event_person.append(person.event_id)
    return db_event_person


def get_participation(db: Session, person_id: int, event_id: int):
    db_participation = db.query(models.Participation) \
        .filter(models.Participation.person_id == person_id) \
        .filter(models.Participation.event_id == event_id) \
        .all()
    return db_participation


def delete_event(db: Session, event_id: int):
    db_event = db.query(models.Event).filter(models.Event.id == event_id).first()
    db.delete(db_event)
    db.commit()
    return True


def delete_participation(db: Session, participation: schemas.Participation):
    db_event = db.query(models.Participation) \
        .filter(models.Participation.event_id == participation.event_id) \
        .filter(models.Participation.person_id == participation.person_id) \
        .first()
    db.delete(db_event)
    db.commit()
    return True
