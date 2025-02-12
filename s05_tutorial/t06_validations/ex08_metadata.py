from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(
    q: str 
    | None 
    = Query(
        default = None, 
        title = "Titulo de prueba", 
        description= "Descripcion de prueba", 
        min_length = 3,
        alias="q-alias")
    ):
    results = {
        "items": [
            {"item_id": "ABC"},
            {"item_id": "XYZ"}
        ]
    }

    if q:
        results.update({"q": q})

    return results