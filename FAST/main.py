from fastapi import FastAPI, HTTPException
from typing import Optional

app= FastAPI(
    title="Mi primer API",
    description="Arath Josue Perez Campos",
    version="1.0.0",
)

usuarios=[
    {"id":1,"nombre":"Arath","edad":20},
    {"id":2,"nombre":"Josue","edad":22},
    {"id":3,"nombre":"Jacinto","edad":25},
    {"id":4,"nombre":"Abraham","edad":36}
]

#ruta o ENDPOINT
@app.get('/',tags=['Inicio'])
def home():
    return {'hello': 'world fastApi'}

#ENDPOINTConsulta Todos
@app.get('/todosUsuarios',tags=['Operaciones CRUD'])
def leer():
    return {'Usuarios Registrados': usuarios}

#ENDPOINT POST
@app.post('/usuarios/',tags=['Operaciones CRUD'])
def guardar(usuario:dict):
    for usr in usuarios:
        if usr['id'] == usuario.get('id'):
            raise HTTPException(status_code=400,detail="El usuario ya existe")
    usuarios.append(usuario)
    return usuario

#ENDPOINT para actualizar
@app.put('/usuarios/{id}',tags=['Operaciones CRUD'])
def actualizar(id:int,usuarioActualizado:dict):
    for index, usr in enumerate(usuarios):
        if usr['id'] == id:
            usuarios[index].update(usuarioActualizado)
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