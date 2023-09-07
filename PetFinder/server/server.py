from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pet_finder_client import PetFinderClient
from models.animal import Animal
from pathlib import Path

# should be saved in a secure place
client_id = "Umcqw6TWPCwhteNyMqJNLJEeasrecM3RcTHZRJQWQjwBfzgzl9"
client_secret = "lw1oCR5FgETXi6y2YEzmj2WZ1TVE6sGkIdy6E0o8"

pet_finder_client = PetFinderClient(client_id=client_id, client_secret=client_secret)

cur_animals: list[dict[str, int | str | None]] = None # type: ignore
cur_type: str = ""
cur_page: int = 0
cur_last_page: int = 0

app = FastAPI()

img_path = Path('models')

# Configure CORS such that my local frontend client can request from this server
origins = [
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def update_info(type: str, page: int) -> bool:
    global cur_type, cur_page, cur_animals
    if type != cur_type or page != cur_page:
        cur_type = type
        cur_page = page
        return True
    return False

@app.get('/')
async def root() -> List[str]:
    return pet_finder_client.get_animal_types()

@app.get('/{type}/{page}')
async def get_animals(type: str, page: int) -> tuple[int, list[dict[str,int | str | None]]]:
    global cur_animals, cur_last_page
    if update_info(type, page):
        response = pet_finder_client.get_animals(cur_type, cur_page)
        cur_last_page = response[0]['total_pages']
        animals = response[1]
        cur_animals = [{'id': item.id, 'name': item.name, 'description': item.description, 'imgURL': item.photos[0].small} for item in animals]
    return (cur_last_page, cur_animals)

@app.get('/{type}/{page}/{id}')
async def get_animal_by_ID(type: str, page: int, id: int) -> Animal:
    global cur_animals, cur_last_page
    if update_info(type, page):
        response = pet_finder_client.get_animals(cur_type, cur_page)
        cur_last_page = response[0]['total_pages']
        animals = response[1]
        cur_animals = [{'id': item.id, 'name': item.name, 'description': item.description, 'imgURL': item.photos[0].small} for item in animals]
    return pet_finder_client.get_animal(type, page, id)

@app.get('/no_image')
async def get_no_img():
    return FileResponse(img_path / 'no-img.jpg')