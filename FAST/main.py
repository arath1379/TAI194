from fastapi import FastAPI
from DB.conexion import engine, Base
from routers.usuarios import routerUsuario
from routers.auth import routerAuth

app = FastAPI(
    title="Mi primer API",
    description="Arath Josue Perez Campos",
    version="1.0.0",
)

Base.metadata.create_all(bind=engine)

# Ruta de inicio
@app.get("/", tags=["Inicio"])
def home():
    return {"hello": "world fastApi"}

app.include_router(routerUsuario)
app.include_router(routerAuth)