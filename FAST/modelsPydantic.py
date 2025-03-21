from pydantic import BaseModel, Field, EmailStr

class modelUsuario(BaseModel):
    name: str = Field(..., min_length=1, max_length=85, description="Solo letras y espacios min 1 max 85")
    age: int = Field(..., gt=0, le=120, description="La edad siempre debe ser positiva y estar entre 1 y 120")
    email: str = Field(..., pattern=r"^[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,6}$", example="username@domain.com.mx", min_length=1, max_length=350, description="Correo válido min 1 max 350 caracteres")

class modelAuth(BaseModel):
    passw: str = Field(..., min_length=8, strip_whitespace=True,description="Solo letras sin espacion min 8")
    mail: EmailStr