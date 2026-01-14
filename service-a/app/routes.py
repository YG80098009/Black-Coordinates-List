from fastapi import APIRouter
from app.services import get_my_ip, get_coordinates, send_to_service_b

router = APIRouter()

@router.get("/process/{ip_}")
def process_ip(ip_):
    ip = get_my_ip(ip_)
    coords = get_coordinates(ip)
    result = send_to_service_b(coords)

    return {
        "ip": ip,
        "coordinates": coords,
        "service_b_response": result
    }