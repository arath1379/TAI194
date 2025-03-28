from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from modelsPydantic import modelUsuario
from middlewares import BearerJWT
from DB.conexion import Session
from models.modelsDB import User
from fastapi import APIRouter

routerUsuario = APIRouter()

# ENDPOINT - Obtener todos los usuarios
@routerUsuario.get("/todosUsuarios", tags=["Operaciones CRUD"])
def leer():
    db = Session()
    try:
        consulta = db.query(User).all()
        return JSONResponse(content=jsonable_encoder(consulta))
    except Exception as e:
        db.rollback()
        return JSONResponse(
            status_code=500, 
            content={"mensaje": "No fue posible consultar", "Error": str(e)}
        )
    finally:
        db.close()

# ENDPOINT - Obtener un usuario por id
@routerUsuario.get("/usuario/{id}", tags=["Operaciones CRUD"])
def leerOne(id: int):
    db = Session()
    try:
        consulta1 = db.query(User).filter(User.id == id).first()
        if not consulta1:
            return JSONResponse(status_code=404,content={"mensaje":"Usuario no encontrado"})
        return JSONResponse(content=jsonable_encoder(consulta1))
    except Exception as e:
        db.rollback()
        return JSONResponse(
            status_code=500, 
            content={"mensaje": "No fue posible consultar", "Error": str(e)}
        )
    finally:
        db.close()

# ENDPOINT - Agregar usuario
@routerUsuario.post("/usuarios/", response_model=modelUsuario, tags=["Operaciones CRUD"])
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
@routerUsuario.put("/usuarios/{id}", response_model=modelUsuario, tags=["Operaciones CRUD"])
def actualizar_usuario(id: int, usuario_actualizado: modelUsuario):
    db = Session()
    try:
        usuario_db = db.query(User).filter(User.id == id).first()
        if not usuario_db:
            return JSONResponse(status_code=404, content={"mensaje": "Usuario no encontrado"})
        
        for key, value in usuario_actualizado.model_dump().items():
            setattr(usuario_db, key, value)
        
        db.commit()
        db.refresh(usuario_db)
        return JSONResponse(content=jsonable_encoder(usuario_db))
    except Exception as e:
        db.rollback()
        return JSONResponse(
            status_code=500,
            content={"mensaje": "No fue posible actualizar", "Error": str(e)}
        )
    finally:
        db.close()

# ENDPOINT - Eliminar usuario
@routerUsuario.delete("/usuarios/{id}", tags=["Operaciones CRUD"])
def eliminar_usuario(id: int):
    db = Session()
    try:
        usuario_db = db.query(User).filter(User.id == id).first()
        if not usuario_db:
            return JSONResponse(status_code=404, content={"mensaje": "Usuario no encontrado"})
        
        db.delete(usuario_db)
        db.commit()
        return JSONResponse(content={"mensaje": "Usuario eliminado con éxito"})
    except Exception as e:
        db.rollback()
        return JSONResponse(
            status_code=500,
            content={"mensaje": "No fue posible eliminar", "Error": str(e)}
        )
    finally:
        db.close()