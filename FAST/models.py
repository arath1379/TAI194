from pydantic import BaseModel, Field

class modelUsuario(BaseModel):
    id: int = Field(..., gt=0, description="Id siempre debe de ser positivo") 
    nombre: str = Field(..., min_length=1, max_length=85, description="Solo letras y espacios min 1 max 85")
    edad: int = Field(..., gt=0, le=120, description="La edad siempre debe ser positiva y estar entre 1 y 120")
    correo: str = Field(..., pattern=r"^[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,6}$", example="username@domain.com.mx", min_length=1, max_length=350, description="Correo válido min 1 max 350 caracteres")
