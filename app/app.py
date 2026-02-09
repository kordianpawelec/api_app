from fastapi import FastAPI, HTTPException, Depends
from schemas.car import CarInput, CarOutput, TripInput, TripOutput
from db.car import get_session, get_car, get_all_cars, add_car, db_delete_car, update_car, add_trip, delete_trip, Session
from typing import List, Annotated

import uvicorn


# def open_session():
#     return next(session())





app = FastAPI()


@app.get('/api/car/{car_id}')
def get_cars(session: Annotated[Session, Depends(get_session)], car_id: int) -> CarOutput:
    result = get_car(session, car_id)
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail=f'No car with id={car_id}')


@app.get('/api/cars')
def get_cars(session: Annotated[Session, Depends(get_session)], size: str|None = None, doors: int|None = None) -> List[CarInput]:
    result = get_all_cars(session)
    if size:
        result = [car for car in result if car.size == size]
    if doors:
        result = [car for car in result if car.doors >= doors]
    return result


@app.post('/api/cars')
def add_car_new(session: Annotated[Session, Depends(get_session)], car: CarInput) -> CarOutput:
    return add_car(session, car)


@app.delete('/api/delete/{car_id}', status_code=204)
def delete_car(session: Annotated[Session, Depends(get_session)], car_id: int) -> None:
    result = db_delete_car(session, car_id)
    if result:
        pass
    else:
        raise HTTPException(status_code=404, detail=f'car donet exist with car_id={car_id}')


@app.put('/api/cars/{car_id}')
def update_old_car(session: Annotated[Session, Depends(get_session)], car: CarInput, car_id: int):
    result = update_car(session, car, car_id)
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail=f'No car with car_id:{car_id}')


@app.post('/api/cars/{car_id}/trips')
def add_a_trip(session: Annotated[Session, Depends(get_session)], car_id: int, trip: TripInput):
    new_trip = add_trip(session, car_id, trip)
    if new_trip:
        return new_trip
    raise HTTPException(status_code=404, detail='car_id not found')




if __name__ == "__main__":
    uvicorn.run('app:app', reload=True)