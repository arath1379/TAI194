from fastapi.responses import JSONResponse
from modelsPydantic import modelAuth
from genToken import createToken
from fastapi import APIRouter

routerAuth = APIRouter()

# Endpoint para generar token
@routerAuth.post("/auth", tags=["Autenticación"])
def auth(credenciales: modelAuth):
    if credenciales.mail == "arath@example.com" and credenciales.passw == "123456789":
        token: str = createToken(credenciales.model_dump())
        print(token)
        return JSONResponse(content=token)
    else:
        return {"Aviso": "Usuario no cuenta con permiso"}

