from fastapi import FastAPI
from schemas.car import load_db
import uvicorn

app = FastAPI()
db = load_db()

@app.get('/api/car/{car_id}')
def get_cars(car_id: int):
    for car in db:
        if car.get('id') == car_id:
            return car
        
        
@app.get('/cars')
def get_cars():
    return db


if __name__ == "__main__":
    uvicorn.run('app:app', reload=True)