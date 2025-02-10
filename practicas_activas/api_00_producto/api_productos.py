from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import uuid4 as uuid

# Clase producto
class Producto(BaseModel):
    id: str | None = None
    nombre: str
    precio_compra: float
    precio_venta: float
    proveedor: str

# Se crea la API
app = FastAPI()

# Lista donde irán todos los productos
productos = []

# Mensaje de bienvenida
@app.get("/")
def index():
    return {"mensaje": "Bienvenidos a la API de Productos"}

# Leer productos
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
    resultado = list(filter(lambda p: p.id == producto_id, productos))

    # Si se encuentra un producto
    if len(resultado):
        return resultado[0]

    # Si no encuentran un producto
    # return {"mensaje": f"El producto con el ID {producto_id} no fue encontrado"}
    raise HTTPException(status_code = 404, detail="El producto con el ID {producto_id} no fue encontrado")

# Eliminar productos a partir de un id
@app.delete("/producto/{producto_id}")
def eliminar_producto_por_id(producto_id: str):
    resultado = list(filter(lambda p: p.id == producto_id, productos))

    # Si se encuentra un producto
    if len(resultado):
        producto_encontrado = resultado[0]
        productos.remove(producto_encontrado)

        return {"mensaje": f"El producto con ID {producto_id} fue eliminado"}

    # Si no encuentran un producto
    # return {"mensaje": f"El producto con el ID {producto_id} no fue encontrado"}
    raise HTTPException(status_code = 404, detail="El producto con el ID {producto_id} no fue encontrado")

# Actualizar productos a partir de un id
@app.put("/producto/{producto_id}")
def actualizar_producto(producto_id: str, producto: Producto):
    resultado = list(filter(lambda p: p.id == producto_id, productos))

    # Si se encuentra un producto
    if len(resultado):
        producto_encontrado = resultado[0]
        producto_encontrado.nombre = producto.nombre
        producto_encontrado.precio_compra = producto.precio_compra
        producto_encontrado.precio_venta = producto.precio_venta
        producto_encontrado.proveedor = producto.proveedor

        return producto_encontrado

    # Si no encuentran un producto
    # return {"mensaje": f"El producto con el ID {producto_id} no fue encontrado"}
    raise HTTPException(status_code = 404, detail="El producto con el ID {producto_id} no fue encontrado")