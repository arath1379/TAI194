from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from typing import Optional, List
from modelsPydantic import modelUsuario
from modelsPydantic import modelAuth
from genToken import createToken
from middlewares import BearerJWT
from DB.conexion import Session, engine, Base
from models.modelsDB import User

app = FastAPI(
    title="Mi primer API",
    description="Arath Josue Perez Campos",
    version="1.0.0",
)

Base.metadata.create_all(bind=engine)

usuarios = [
    {"id": 1, "nombre": "Arath", "edad": 20, "correo": "arath@example.com"},
    {"id": 2, "nombre": "Josue", "edad": 22, "correo": "josue@example.com"},
    {"id": 3, "nombre": "Jacinto", "edad": 25, "correo": "jaci@example.com"},
    {"id": 4, "nombre": "Joel", "edad": 21, "correo": "joel@example.com"},
]

# Ruta de inicio
@app.get("/", tags=["Inicio"])
def home():
    return {"hello": "world fastApi"}

# Endpoint para generar token
@app.post("/auth", tags=["Autenticación"])
def auth(credenciales: modelAuth):
    if credenciales.mail == "arath@example.com" and credenciales.passw == "123456789":
        token: str = createToken(credenciales.model_dump())
        print(token)
        return JSONResponse(content=token)
    else:
        return {"Aviso": "Usuario no cuenta con permiso"}

# ENDPOINT - Obtener todos los usuarios
@app.get("/todosUsuarios", dependencies=[Depends(BearerJWT())],response_model=List[modelUsuario], tags=["Operaciones CRUD"])
def leer():
    return usuarios

# ENDPOINT - Agregar usuario
@app.post("/usuarios/", response_model=modelUsuario, tags=["Operaciones CRUD"])
def guardar(usuario: modelUsuario):
    db = Session()
    try:
        nuevo_usuario = User(**usuario.model_dump())  # Desempaqueta el diccionario
        db.add(nuevo_usuario)
        db.commit()
        return JSONResponse(
            status_code=201, 
            content={"mensaje": "Usuario Guardado", "usuario": usuario.model_dump()}
        )
    except Exception as e:
        db.rollback()
        return JSONResponse(
            status_code=500, 
            content={"mensaje": "No fue posible guardar", "Error": str(e)}
        )
    finally:
        db.close()

# ENDPOINT - Actualizar usuario
@app.put("/usuarios/{id}", response_model=modelUsuario, tags=["Operaciones CRUD"])
def actualizar(id: int, usuarioActualizado: modelUsuario):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index] = usuarioActualizado.model_dump()
            return usuarios[index]
    raise HTTPException(status_code=400, detail="El usuario no existe")

# ENDPOINT - Eliminar usuario
@app.delete("/usuarios/{id}", tags=["Operaciones CRUD"])
def eliminar(id: int):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios.pop(index)
            return {"Mensaje": "Usuario eliminado con éxito"}
    raise HTTPException(status_code=400, detail="El usuario no existe")
