from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items")
async def read_items(q: str | None = Query(default = None, max_length = 5, min_length = 3)):
    results = {
        "items": [
            {"item_id": "ABC"},
            {"item_id": "123"}
        ]
    }

    if q:
        results.update({"q": q})

    return results