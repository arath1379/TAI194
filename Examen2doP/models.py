from pydantic import BaseModel, Field

class modelVehiculo(BaseModel):
    id_vehiculo: int = Field(..., gt=0,description="Id del vehiculo siempre positivo")
    año: int = Field(..., gt=4, description="año debe ser mayor a 4 digitos") 
    modelo: str = Field(...,min_leght=4, max_leght=25, description="modelo string min 4 letras max 25")
    placa: str = Field(..., max_leght=10, description="Placa string max 10 letras")
