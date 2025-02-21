from fastapi import FastAPI, HTTPException
from typing import Optional, List
from pydantic import BaseModel

app= FastAPI(
    title="Mi primer API",
    description="Arath Josue Perez Campos",
    version="1.0.0",
)

class modelUsuario(BaseModel):
    id: int
    nombre: str
    edad: int
    correo: str

usuarios=[
    {"id":1,"nombre":"Arath","edad":20,"correo":"arath@example.com"},
    {"id":2,"nombre":"Josue","edad":22,"correo":"josue@example.com"},
    {"id":3,"nombre":"Jacinto","edad":25,"correo":"jaci@example.com"},
    {"id":4,"nombre":"Joel","edad":21,"correo":"joel@example.com"}
]

#ruta o ENDPOINT
@app.get('/',tags=['Inicio'])
def home():
    return {'hello': 'world fastApi'}

#ENDPOINTConsulta Todos
@app.get('/todosUsuarios',response_model=List[modelUsuario],tags=['Operaciones CRUD'])
def leer():
    return usuarios

#ENDPOINT POST
@app.post('/usuarios/',response_model=modelUsuario,tags=['Operaciones CRUD'])
def guardar(usuario:modelUsuario):
    for usr in usuarios:
        if usr['id'] == usuario.id:
            raise HTTPException(status_code=400,detail="El usuario ya existe")
    usuarios.append(usuario)
    return usuario

#ENDPOINT para actualizar
@app.put('/usuarios/{id}',response_model=modelUsuario,tags=['Operaciones CRUD'])
def actualizar(id:int,usuarioActualizado:modelUsuario):
    for index, usr in enumerate(usuarios):
        if usr['id'] == id:
            usuarios[index]== usuarioActualizado.model_dump()
            return usuarios[index]
    raise HTTPException(status_code=400,detail="El usuario no existe")

#ENDPOINT para eliminar
@app.delete('/usuarios/{id}',tags=['Operaciones CRUD'])
def eliminar(id:int):
    for index, usr in enumerate(usuarios):
        if usr['id'] == id:
            usuarios.pop(index)
            return {'Mensaje':'Usuario eliminado con exito'}
    raise HTTPException(status_code=400,detail="El usuario no existe")