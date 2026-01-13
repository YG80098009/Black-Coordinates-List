from pydantic import BaseModel, Field

class Coordinates(BaseModel):
    ip: str = Field(..., description="IP address")
    latitude: float = Field(..., description="Latitude")
    longitude: float = Field(..., description="Longitude")
