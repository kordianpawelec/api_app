from pydantic import BaseModel
from enum import StrEnum
from typing import List
import json

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

class Car(BaseModel):
    id: int
    size: Size
    fuel: Fuel | None = Fuel.GASOLINE
    doors: int 
    transmission: Transmission | None = Transmission.MANUAL


def load_db() -> List[Car]:
    with open('cars.json') as f:
        return [Car(**obj) for obj in json.load(f)]