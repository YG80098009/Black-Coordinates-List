from pydantic import BaseModel, IPvAnyAddress


class Coordinates(BaseModel):
    ip: IPvAnyAddress
    lat: float
    lon: float

    