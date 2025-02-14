from fastapi import FastAPI, HTTPException
from typing import Optional

app= FastAPI(
    title="API de Gestion de Tareas To-Do List",
    description="Arath Josue Perez Campos",
    version="2.0.0",
)

tareas = [
    {"id": 1, "nombre": "Estudiar para examen", "descripcion": "Repasar apuntes de TAI", "vencimiento": "14-02-24", "estado": "completada"},
    {"id": 2, "nombre": "Hacer ejercicio", "descripcion": "Correr 5km en el parque", "vencimiento": "19-02-25", "estado": "no completada"},
    {"id": 3, "nombre": "Comprar víveres", "descripcion": "Lista: leche, pan, huevos", "vencimiento": "20-02-25", "estado": "no completada"},
    {"id": 4, "nombre": "Terminar proyecto", "descripcion": "Finalizar el código y documentar", "vencimiento": "21-02-25", "estado": "no completada"},
    {"id": 5, "nombre": "Leer un libro", "descripcion": "Avanzar 50 páginas de 'El principito'", "vencimiento": "22-02-25", "estado": "completada"}
]

#EndPoint para Obtener todas las tareas.
@app.get('/tareas',tags=['Gestion Tareas'])
def ObtenerTodasLasTareas():
    return {'Tareas Registradas': tareas}

#EndPoint para Obtener una tarea específica por su ID.
@app.get('/tareas/{id}',tags=['Gestion Tareas'])
def ObtenerTareaEspecifica(id: int):
    for tarea in tareas:
        if tarea['id'] == id:
            return tarea
    raise HTTPException(status_code=404, detail="Tarea no encontrada")
    

#EndPoint para Crear una nueva tarea.
@app.post('/tareas',tags=['Gestion Tareas'])
def CrearNuevaTarea(tarea: dict):
    for tarea in tareas:
        if tarea['id'] == id:
            return {'Tarea': tarea}
        raise HTTPException(status_code=400,detail="La tarea ya existe")
    tareas.append(tarea)
    return tarea