from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException, status
from sqlmodel import Session, select
from .database import crear_tablas, obtener_sesion
from .models import Producto, ProductoCrear, ProductoActualizar, ProductoLeer


@asynccontextmanager
async def lifespan(app: FastAPI):
    crear_tablas()
    yield


app = FastAPI(title="API de Productos", version="1.0.0", lifespan=lifespan)


@app.get("/")
def inicio():
    return {"mensaje": "Bienvenidos a la API de productos"}


@app.get("/api/productos/", response_model=list[ProductoLeer])
def listar_productos(sesion: Session = Depends(obtener_sesion)):
    return sesion.exec(select(Producto)).all()


@app.get("/api/productos/{producto_id}/", response_model=ProductoLeer)
def obtener_producto(producto_id: int, sesion: Session = Depends(obtener_sesion)):
    producto = sesion.get(Producto, producto_id)
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto


@app.post("/api/productos/", response_model=ProductoLeer, status_code=status.HTTP_201_CREATED)
def crear_producto(datos: ProductoCrear, sesion: Session = Depends(obtener_sesion)):
    producto = Producto.model_validate(datos)
    sesion.add(producto)
    sesion.commit()
    sesion.refresh(producto)
    return producto


@app.put("/api/productos/{producto_id}/", response_model=ProductoLeer)
def actualizar_producto(producto_id: int, datos: ProductoActualizar, sesion: Session = Depends(obtener_sesion)):
    producto = sesion.get(Producto, producto_id)
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    producto.sqlmodel_update(datos.model_dump())
    sesion.add(producto)
    sesion.commit()
    sesion.refresh(producto)
    return producto


@app.delete("/api/productos/{producto_id}/", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_producto(producto_id: int, sesion: Session = Depends(obtener_sesion)):
    producto = sesion.get(Producto, producto_id)
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    sesion.delete(producto)
    sesion.commit()
    return None
