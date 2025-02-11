from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}/items/{item_id}")
async def read_items(user_id: int, item_id: str, q: str | None = None, short: bool = False):
    item = {"owner_id": user_id, "item_id": item_id}
    if q:
        item.update({"item_id": item_id, "q": q})
    if not short:
        item.update({"description": "Python and FastAPI"})
    return item