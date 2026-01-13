from pydantic import BaseModel


class Coordinats(BaseModel):
    ip: str
    lat: int
    lon: int