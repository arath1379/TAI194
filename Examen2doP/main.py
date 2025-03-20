from fastapi import FastAPI, HTTPException
from models import modelVehiculo
from typing import List

app = FastAPI(
    title="Gestión Vehículos",
    description="Arath Josue Perez Campos",
    version="3.0.0",
)

# Lista de vehículos
vehiculos = [
    {"id_vehiculo": 1, "modelo": "Corolla", "año": 2020, "placa": "2Gytsa8AS"},
    {"id_vehiculo": 2, "modelo": "Civic", "año": 2019, "placa": "Hgb6689VC"},
    {"id_vehiculo": 3, "modelo": "Sentra", "año": 2018, "placa": "H98BNjgO88"}
]

# Obtener todos los vehículos
@app.get("/vehiculos", tags=["Vehiculos"])
def obtener_vehiculos():
    return vehiculos

# Guardar un nuevo vehículo
@app.post("/vehiculos", response_model=modelVehiculo, tags=["Vehiculos"])
def crear_vehiculo(vehiculo: modelVehiculo):
    vehiculos.append(vehiculo.dict())
    return vehiculo

# Actualizar un vehículo
@app.put("/vehiculos/{id}", response_model=modelVehiculo, tags=["Vehiculos"])
async def actualizar_vehiculo(id: int, vehiculo: modelVehiculo):
    for v in vehiculos:
        if v["id_vehiculo"] == id:
            v["modelo"] = vehiculo.modelo
            v["año"] = vehiculo.año
            v["placa"] = vehiculo.placa
            return v
    raise HTTPException(status_code=404, detail="Vehículo no encontrado")
