from pydantic import BaseModel, Field

class Coordinates(BaseModel):
    ip: str = Field(..., description="IP address")
    lat: float = Field(..., description="Latitude")
    lon: float = Field(..., description="Longitude")
