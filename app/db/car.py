from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models.car import Car, Base, Trip
from schemas.car import CarInput, CarOutput, TripInput, TripOutput


engine = create_engine(
    "sqlite:///carsharing.db",
    connect_args={"check_same_thread": False},
    echo=True
)


Base.metadata.create_all(engine)


def get_session():
    # return Session(engine)
    with Session(engine) as session:
        yield session


def get_car(session: Session, car_id: int) -> CarOutput | None:
    car = session.query(Car).filter(Car.id == car_id).first()
    if car:
        return CarOutput.model_validate(car)
    return None


def get_all_cars(session: Session) -> list[CarOutput]:
    cars = session.query(Car).all()
    if cars:
        return [CarOutput.model_validate(car) for car in cars]
    return []


def add_car(session: Session, car: CarInput) -> CarOutput:
    new_car = Car(
        size=car.size,
        doors=car.doors,
        transmission=car.transmission,
        fuel=car.fuel
    )
    session.add(new_car)
    session.commit()
    session.refresh(new_car)
    return CarOutput.model_validate(new_car)


def update_car(session: Session, new_car: CarInput, car_id: int) -> CarOutput | None:
    car = session.get(Car, car_id)
    if car:
        for k, v in new_car.model_dump().items():
            setattr(car, k, v)
        session.commit()
        session.refresh(car)
        return CarOutput.model_validate(car)
    return None


def db_delete_car(session: Session, car_id: int) -> bool:
    car = session.get(Car, car_id)
    if car:
        session.delete(car)
        session.commit()
        return True
    return False


def add_trip(session: Session, car_id: int, trip: TripInput) -> TripOutput | None:
    car = session.get(Car, car_id)
    if car:
        new_trip = Trip(**trip.model_dump(), car_id=car_id)
        car.trips.append(new_trip)
        session.commit()
        session.refresh(new_trip)
        return TripOutput.model_validate(new_trip)
    return None


def delete_trip(session: Session, car_id: int, trip_id: int) -> bool:
    trip = session.query(Trip).filter(Trip.id == trip_id, Car.id == car_id).first()
    if trip:
        session.delete(trip)
        session.commit()
        return True
    return False