
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
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

