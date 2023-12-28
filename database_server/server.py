from typing import List, Dict, Any
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pet_finder_client import PetFinderClient
from pathlib import Path
from database import getConn, close

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
origins: list[str] = [
    "http://localhost:3000",
]
app.add_middleware(
    middleware_class=CORSMiddleware,
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

conn, dicCur, cur = getConn()
def ini():
    global conn, cur
    types = pet_finder_client.get_animal_types()
    cur.execute('DROP TABLE IF EXISTS types;')
    cur.execute('''
        CREATE TABLE types(
                type            VARCHAR(20),
                totalPages      INT
        );
    ''')
    for type in types:
        cur.execute(f'DROP TABLE IF EXISTS "{type}"')
        cur.execute('INSERT INTO types(type, totalPages) VALUES(%(t)s, 0)', {'t': type})
        cur.execute(f'''
            CREATE TABLE "{type}"(
                    id              INT,
                    name            TEXT,
                    type            VARCHAR(20) DEFAULT '{type}',
                    page            INT,
                    description     TEXT,
                    "smallImage"    TEXT,
                    "fullImage"     TEXT
            )
        ''')
    conn.commit()
ini()
@app.get('/')
async def root() -> List[str]:
    global cur
    cur.execute('SELECT type from types')
    return [t[0] for t in cur.fetchall()]

@app.get('/{type}/{page}')
async def get_animals(type: str, page: int) -> tuple[int, list[Dict[str, int | str]]]:
    global conn, dicCur, cur
    cur.execute(f'SELECT COUNT(*) FROM "{type}" WHERE page={page}')
    if(cur.fetchall()[0][0] == 0):
        response = pet_finder_client.get_animals(type, page)
        cur.execute(f'UPDATE types SET totalPages={response[0]["total_pages"]}')
        for animal in response[1]:
            cur.execute(f'''INSERT INTO "{type}"(id, name, page, description, "smallImage", "fullImage") VALUES({animal.id}, '{animal.name}', {page}, '{animal.description}', '{animal.photos[0].small}', '{animal.photos[0].full}')''')
    conn.commit()
    cur.execute('SELECT totalPages FROM types')
    totalPages:int = cur.fetchall()[0][0]
    dicCur.execute(f'SELECT * FROM "{type}" WHERE page={page}')
    animals: List[Dict[str, str|int]] = dicCur.fetchall() #type: ignore
    cur_animals:List[Dict[str, int|str]] = [{'id': item['id'], 'name': item['name'], 'description': item['description'], 'imgURL': item['smallImage']} for item in animals]
    return (totalPages, cur_animals)

@app.get('/{type}/{page}/{id}')
async def get_animal_by_ID(type: str, page: int, id: int):
    global dicCur
    dicCur.execute(f'SELECT * FROM "{type}" WHERE id={id}')
    result = dict(dicCur.fetchall()[0])
    print(result)
    return result

@app.get('/no_image')
async def get_no_img():
    return FileResponse(img_path / 'no-img.jpg')

@app.get('/refresh')
async def refreshDB():
    ini()

@app.on_event("shutdown")
def shutdown_event():
    global conn, dicCur, cur
    close(conn, dicCur, cur)