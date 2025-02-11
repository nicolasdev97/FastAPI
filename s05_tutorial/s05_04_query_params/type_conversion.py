from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"item_id": item_id, "q": q})
    if not short:
        item.update({"description": "Python and FastAPI"})
    return item