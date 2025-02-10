from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4 as uuid

# Clase producto
class Producto(BaseModel):
    id: str | None = None
    nombre: str
    precio_compra: float
    precio_venta: float
    proveedor: str

# Se define la API
app =FastAPI()

# Pendiente
productos = []

# Mensaje de bienvenida
@app.get("/")
def index():
    return {"mensaje": "Bienvenidos a la API de Productos"}

# Listar productos
@app.get("/producto")
def obtener_productos():
    return productos

# Crear productos
@app.post("/producto")
def crear_producto(producto: Producto):
    producto.id = str(uuid()) # Genera un id unico para el producto
    productos.append(producto)
    return {"mensaje": "Producto creado satisfactoriamente"}

# Buscar productos a partir de un id
@app.get("/producto/{producto_id}")
def obtener_producto_por_id(producto_id: str):
    for producto in productos:
        if producto.id == producto_id:
            return producto

    # Si no encuentran un producto con ese id    
    return {"mensaje": f"El producto con el ID {producto_id} no fue encontrado"}