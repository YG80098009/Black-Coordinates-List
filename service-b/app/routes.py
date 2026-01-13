from fastapi import APIRouter
from app.schemas import Coordinates
from app.storage import save_coordinates, get_all_coordinates

router = APIRouter()

@router.post("/store")
def store_coordinates(coords: Coordinates):
    save_coordinates(coords.dict())
    return {"status": "saved"}


@router.get("/all")
def get_coordinates():
    return get_all_coordinates()
