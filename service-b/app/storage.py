import os
import redis
import json

redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = int(os.getenv("REDIS_PORT", 6379))

r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

KEY = "coordinates_list"

def save_coordinates(data: dict):
    r.rpush(KEY, json.dumps(data))


def get_all_coordinates():
    items = r.lrange(KEY, 0, -1)
    return [json.loads(item) for item in items]
