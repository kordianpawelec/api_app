from pydantic import BaseModel, ConfigDict
from enum import StrEnum


class Size(StrEnum):
    LARGE = 'l'
    MEDIUM = 'm'
    SMALL = 's'

class Fuel(StrEnum):
    GASOLINE = 'gasoline'
    DIESEL = 'diesel'
    ELECTRIC = 'electric'
    HYBRID = 'hybrid'

class Transmission(StrEnum):
    AUTOMATIC = 'auto'
    MANUAL = 'manual'

class Base(BaseModel):
    model_config = ConfigDict(from_attributes=True)

class CarInput(Base):
    size: Size
    fuel: Fuel | None = Fuel.GASOLINE
    doors: int 
    transmission: Transmission | None = Transmission.MANUAL
    
class TripInput(Base):
    start: int
    end: int
    description: str


class TripOutput(TripInput):
    id: int


class CarOutput(CarInput):
    id: int
    trips: list[TripOutput] | list = []
