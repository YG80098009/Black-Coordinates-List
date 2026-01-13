from pydantic import BaseModel


class Coordinats(BaseModel):
    ip: str
    lat: float
    lon: float