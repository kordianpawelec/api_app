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

class CarInput(BaseModel):
    size: Size
    fuel: Fuel | None = Fuel.GASOLINE
    doors: int 
    transmission: Transmission | None = Transmission.MANUAL
    
    model_config = ConfigDict(from_attributes=True)

class CarOutput(CarInput):
    id: int
