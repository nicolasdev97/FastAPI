from fastapi import FastAPI, Query, Path

app = FastAPI()

# El * al principio de los parametros indica que todos deben ser argumentos llave-valor
# El ... al principio de Path() indica que es obligatorio
# El ge=1 indica que debe ser igual o mayor a 1
# El le=1 indica que debe ser igual o menos a 1
# El eq=1 indica que debe ser igual a 1
@app.get("/items/{item_id}")
async def read_items(*, item_id: int = Path(..., title="Path title example", eq=1),
                     q: str | None = Query(default=None, alias="q-alias")):
    results = {"item_id": item_id}

    if q:
        results.update({"q": q})
    
    return results