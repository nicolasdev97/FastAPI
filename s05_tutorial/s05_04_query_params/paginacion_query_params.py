from fastapi import FastAPI

app = FastAPI()

fake_items_db = [
    {"item_name": "foo"},
    {"item_name": "bar"},
    {"item_name": "baz"}
]

# La consulta trae los elementos 
# El skip indica cuantos elementos se van a saltar, en este caso 0
# El limit indica cuando elemento se van a tomar a partir del skip
# Si skip vale 5, se saltan los primeros 5 elementos
# Y si limit vale 3, se toman los siguientes 3 elementos
@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]