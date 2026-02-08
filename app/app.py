from fastapi import FastAPI, HTTPException
from schemas.car import CarInput, CarOutput
from db.car import session, engine, get_car, get_all_cars, add_car, db_delete_car, update_car
from typing import List
from models.car import Base
from contextlib import asynccontextmanager



import uvicorn


def open_session():
    return next(session())


async def lifespan(app: FastAPI):
    Base.metadata.create_all(engine)
    yield


app = FastAPI(lifespan=lifespan)


@app.get('/api/car/{car_id}')
def get_cars(car_id: int) -> CarOutput:
    result = get_car(open_session(), car_id)
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail=f'No car with id={car_id}')


@app.get('/api/cars')
def get_cars(size: str|None = None, doors: int|None = None) -> List[CarInput]:
    result = get_all_cars(open_session())
    if size:
        result = [car for car in result if car.size == size]
    if doors:
        result = [car for car in result if car.doors >= doors]
    return result


@app.post('/api/cars/')
def add_car_new(car: CarInput) -> CarOutput:
    return add_car(open_session(), car)


@app.delete('/api/delete/{car_id}', status_code=204)
def delete_car(car_id: int) -> None:
    result = db_delete_car(open_session(), car_id)
    if result:
        pass
    else:
        raise HTTPException(status_code=404, detail=f'car donet exist with car_id={car_id}')


@app.put('/api/cars/{car_id}')
def update_old_car(car: CarInput, car_id: int):
    result = update_car(open_session(), car, car_id)
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail=f'No car with car_id:{car_id}')

if __name__ == "__main__":
    uvicorn.run('app:app', reload=True)