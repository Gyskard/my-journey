from fastapi import Depends, FastAPI, HTTPException, status
from fastapi_responses import custom_openapi
from sqlalchemy.orm import Session

from modules import models, crud, schemas
from modules.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.openapi = custom_openapi(app)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Server is online!"}


@app.put("/location", status_code=201)
async def create_location(location: schemas.Location, db: Session = Depends(get_db)):
    db_location = crud.get_location_by_all_infos(db=db, location=location)
    if db_location:
        raise HTTPException(status_code=400, detail="Location already exists")
    db_location = crud.create_location(db=db, location=location)
    if not db_location:
        raise HTTPException(status_code=500, detail="Location not created")
    return status.HTTP_201_CREATED


@app.get("/location", response_model=schemas.LocationResponse)
async def get_location_by_all_infos(location: schemas.Location, db: Session = Depends(get_db)):
    db_location = crud.get_location_by_all_infos(db=db, location=location)
    if not db_location:
        raise HTTPException(status_code=404, detail="Location not exists")
    return db_location


@app.get("/location/{location_id}", response_model=schemas.LocationResponse)
async def get_location_by_id(location_id: int, db: Session = Depends(get_db)):
    db_location = crud.get_location_by_id(db=db, location_id=location_id)
    if not db_location:
        raise HTTPException(status_code=404, detail="Location not exists")
    return db_location


@app.delete("/location/{location_id}", status_code=200)
async def delete_location(location_id: int, db: Session = Depends(get_db)):
    db_location = crud.get_location_by_id(db=db, location_id=location_id)
    if not db_location:
        raise HTTPException(status_code=404, detail="Location not exists")
    crud.delete_location_by_id(db=db, location_id=location_id)
    db_location = crud.get_location_by_id(db=db, location_id=location_id)
    if db_location:
        raise HTTPException(status_code=500, detail="Location not deleted")
    return status.HTTP_200_OK


@app.put("/person", status_code=201)
async def create_person(person: schemas.Person, db: Session = Depends(get_db)):
    db_person = crud.get_person_by_all_infos(db=db, person=person)
    if db_person:
        raise HTTPException(status_code=400, detail="Person already exists")
    db_person = crud.create_person(db=db, person=person)
    if not db_person:
        raise HTTPException(status_code=500, detail="Person not created")
    return status.HTTP_201_CREATED


@app.get("/person", response_model=schemas.PersonResponse)
async def get_person_by_all_infos(person: schemas.Person, db: Session = Depends(get_db)):
    db_person = crud.get_person_by_all_infos(db=db, person=person)
    if not db_person:
        raise HTTPException(status_code=404, detail="Person not exists")
    return db_person


@app.get("/person/{person_id}", response_model=schemas.PersonResponse)
async def get_person_by_id(person_id: int, db: Session = Depends(get_db)):
    db_person = crud.get_person_by_id(db=db, person_id=person_id)
    if not db_person:
        raise HTTPException(status_code=404, detail="Person not exists")
    return db_person


@app.delete("/person/{person_id}", status_code=200)
async def delete_person(person_id: int, db: Session = Depends(get_db)):
    db_person = crud.get_person_by_id(db=db, person_id=person_id)
    if not db_person:
        raise HTTPException(status_code=404, detail="Person not exists")
    db_event_person = crud.get_event_by_person(db=db, person_id=person_id)
    crud.delete_person_by_id(db=db, person_id=person_id)
    db_person = crud.get_person_by_id(db=db, person_id=person_id)
    if db_person:
        raise HTTPException(status_code=500, detail="Person not deleted")
    for event_person in db_event_person:
        db_person_event = crud.get_person_by_event(db=db, event_id=event_person)
        if len(db_person_event) == 0:
            # delete event
            print("test")
    return status.HTTP_200_OK


@app.get("/person/event/{person_id}", response_model=list)
async def get_event_by_person(person_id: int, db: Session = Depends(get_db)):
    db_person = crud.get_person_by_id(db=db, person_id=person_id)
    if not db_person:
        raise HTTPException(status_code=404, detail="Person not exists")
    db_event_person = crud.get_event_by_person(db=db, person_id=person_id)
    return db_event_person


@app.put("/event", status_code=201)
async def create_event(event: schemas.Event, db: Session = Depends(get_db)):
    db_location = crud.get_location_by_id(db=db, location_id=event.location_id)
    if not db_location:
        raise HTTPException(status_code=404, detail="Location linked to the event not exist")
    db_event = crud.create_event(db=db, event=event)
    if not db_event:
        raise HTTPException(status_code=500, detail="Event not created")
    return status.HTTP_201_CREATED


@app.get("/event/{event_id}", response_model=schemas.EventResponse)
async def get_event(event_id: int, db: Session = Depends(get_db)):
    db_event = crud.get_event(db=db, event_id=event_id)
    if not db_event:
        raise HTTPException(status_code=404, detail="Event not exists")
    return db_event


@app.get("/event/person/{event_id}", response_model=list)
async def get_person_by_event(event_id: int, db: Session = Depends(get_db)):
    db_event = crud.get_event(db=db, event_id=event_id)
    if not db_event:
        raise HTTPException(status_code=404, detail="Event not exists")
    db_person_event = crud.get_person_by_event(db=db, event_id=event_id)
    return db_person_event


@app.put("/participation", status_code=201)
async def create_participation(participation: schemas.Participation, db: Session = Depends(get_db)):
    db_person = crud.get_person_by_id(db=db, person_id=participation.person_id)
    if not db_person:
        raise HTTPException(status_code=404, detail="Person not exists")
    db_event = crud.get_event(db=db, event_id=participation.event_id)
    if not db_event:
        raise HTTPException(status_code=404, detail="Event not exists")
    db_person_event = crud.get_person_by_event(db=db, event_id=participation.event_id)
    if participation.person_id in db_person_event:
        raise HTTPException(status_code=400, detail="Participation already exists")
    db_participation = crud.create_participation(db=db, participation=participation)
    if not db_participation:
        raise HTTPException(status_code=500, detail="Participation not created")
    return status.HTTP_201_CREATED
