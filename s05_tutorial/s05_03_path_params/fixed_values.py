from enum import Enum

from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is model_name.alexnet:
        return {"model_name": model_name, "message": "Deep Learning"}
    
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all tha images"}
    
    return {"model_name": model_name, "message": "Have some residuals"}