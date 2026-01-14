from pydantic import BaseModel


class Coordinates(BaseModel):
    ip: str
    lat: float
    lon: float

    