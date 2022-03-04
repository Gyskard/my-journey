import math

from sqlalchemy.orm import Session, undefer

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


def get_all_location(db: Session):
    return db.query(models.Location).all()


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


def get_all_person(db: Session):
    return db.query(models.Person).all()


def get_person_by_id(db: Session, person_id: int):
    return db.query(models.Person).filter(models.Person.id == person_id).first()


def delete_person_by_id(db: Session, person_id: int):
    db_person = db.query(models.Person).filter(models.Person.id == person_id).first()
    db.delete(db_person)
    db.commit()
    return True


def create_event(db: Session, event: schemas.Event):
    db_event = models.Event(
        event_name=event.event_name,
        description=event.description,
        date=event.date,
        location_id=event.location_id
    )
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


def create_participation(db: Session, participation: schemas.Participation):
    db_all_participation = []
    for participant in participation.person_id_list:
        db_participation = models.Participation(
            event_id=participation.event_id,
            person_id=participant
        )
        db.add(db_participation)
        db.commit()
        db.refresh(db_participation)
        db_all_participation.append(db_participation)
    return db_all_participation


def get_event(db: Session, event_id: int):
    return db.query(models.Event).filter(models.Event.id == event_id).first()


# Need to be included in get_all_event
def get_event_by_all_infos(db: Session, event: schemas.Event):
    return db.query(models.Event) \
        .filter(models.Event.event_name == event.event_name) \
        .filter(models.Event.description == event.description) \
        .filter(models.Event.date == event.date) \
        .filter(models.Event.location_id == event.location_id) \
        .first()


def get_all_event(db: Session, filter: schemas.Filter):
    events = db.query(models.Event)
    if filter.search is not None:
        events = events.filter(models.Event.event_name.contains(filter.search))
    if filter.dates is not None:
        if len(filter.dates) == 1:
            events = events.filter(models.Event.date == filter.dates[0])
        else:
            events = events.filter(models.Event.date >= filter.dates[0], models.Event.date <= filter.dates[1])
    if filter.order_by == "Ascending":
        events = events.order_by(models.Event.date.asc(), models.Event.event_name.asc())
    elif filter.order_by == "Descending":
        events = events.order_by(models.Event.date.desc(), models.Event.event_name.asc())
    events_page_number = math.ceil(len(events.all()) / 10)
    if filter.offset is not None:
        events = events.offset(filter.offset * 10)
    events = events.limit(10).all()
    return {'events': events, 'events_page_number': events_page_number}


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
