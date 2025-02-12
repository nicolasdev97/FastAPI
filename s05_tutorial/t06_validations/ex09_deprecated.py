from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(
    q: str
    | None = Query(
        default=None,
        alias="item-alias",
        title="item-title",
        description="item-desc",
        min_length=3,
        max_length=20,
        regex="^fixedquery$",
        deprecated=True
    )):
    results = {
        {"item_id": "ABC"},
        {"item_id": "DEF"}
    }
    if q:
        results.update({"q": q})
    return results