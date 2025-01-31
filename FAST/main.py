from fastapi import FastAPI
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

#ruta o ENDPOINT Promedio
@app.get('/promedio', tags=['Mi calificacion TAI'])
def promedio():
    return 10

#ruta o ENDPOINT con parametro obligatorio
@app.get('/usuario/{id}')
def consultausuario(id:int):
    #caso ficticio de busqueda de la BD
    return {"Se encontro el usuario":id}

#ruta o ENDPOINT con parametro opcional
@app.get('/usuario2/', tags=['Parametro Opcional'])
def consultausuario2(id:Optional[int]=None):
    if id is not None: #Viene el id
        for usuario in usuarios: #Itera en la lista 
            if usuario['id'] == id:
                return {"Se encontro el usuario":usuario['nombre']}
        return {"mensaje": f"No se encontro el id: {id}"}
    return{"mensaje": "No se proporciono un id"}

#endpoint con varios parametro opcionales
@app.get("/usuarios/", tags=["3 parámetros opcionales"])
async def consulta_usuarios(
    usuario_id: Optional[int] = None,
    nombre: Optional[str] = None,
    edad: Optional[int] = None
):
    resultados = []

    for usuario in usuarios:
        if (
            (usuario_id is None or usuario["id"] == usuario_id) and
            (nombre is None or usuario["nombre"].lower() == nombre.lower()) and
            (edad is None or usuario["edad"] == edad)
        ):
            resultados.append(usuario)

    if resultados:
        return {"usuarios_encontrados": resultados}
    else:
        return {"mensaje": "No se encontraron usuarios que coincidan con los parámetros proporcionados."}
