
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey
from schemas.car import Transmission, Fuel, Size


class Base(DeclarativeBase):
    pass


class Car(Base):
    __tablename__ = 'cars'
    id: Mapped[int] = mapped_column(primary_key=True)
    size: Mapped[Size] = mapped_column()
    doors: Mapped[int] = mapped_column()
    transmission: Mapped[Transmission] = mapped_column()
    fuel: Mapped[Fuel] = mapped_column()
    trips: Mapped[list["Trip"]] = relationship(back_populates="car", cascade='all, delete-orphan')


class Trip(Base):
    __tablename__ = 'trips'
    id: Mapped[int] = mapped_column(primary_key=True)
    car_id: Mapped[int] = mapped_column(ForeignKey(Car.id))
    car: Mapped["Car"] = relationship(back_populates="trips")
    start: Mapped[int] = mapped_column()
    end: Mapped[int] = mapped_column()
    description: Mapped[str] = mapped_column()