from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(
    hiden_query: str
    | None = Query(
        default=None,
        include_in_schema=False
    )
):
    if hiden_query:
        return {"hide_query": hiden_query}
    else:
        return {"hiden_query": "Not found"}