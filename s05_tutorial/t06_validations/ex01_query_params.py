from fastapi import FastAPI

app = FastAPI()

@app.get("/items")
async def read_items(q: str | None = None):
    results = {
        "items": [
            {"item_id": "ABC"},
            {"item_id": "123"}
        ]
    }

    if q:
        results.update({"q": q})

    return results