from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

# Clase producto
class Producto(BaseModel):
    id: Optional[str]
    nombre: str
    precio_compra: float
    precio_venta: float
    proveedor: str

# Se define la API
app =FastAPI()

productos = []

# Mensaje de bienvenida
@app.get("/")
def index():
    return {"mensaje": "Bienvenidos a la API de Productos"}

# Listar productos
@app.get("/producto")
def obtener_productos():
    return productos