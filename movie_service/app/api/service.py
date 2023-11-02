import os
import httpx

CAST_SERVICE_HOST_URL = 'http://localhost:8002/casts/'

def is_cast_present(cast_id: int):
    cast_id = str(cast_id)
    url = os.environ.get('CAST_SERVICE_HOST_URL') or CAST_SERVICE_HOST_URL
    r = httpx.get(f'{url}{cast_id}')
    return True if r.status_code == 200 else False