from fastapi import FastAPI

app= FastAPI()

#ruta o ENDPOINT
@app.get('/')
def home():
    return {'hello': 'world fastApi'}

#ruta o ENDPOINT Promedio
@app.get('/promedio')
def promedio():
    return 10

#ruta o ENDPOINT con parametro obligatorio
@app.get('/usuario/{id}')
def consultausuario(id:int):
    #caso ficticio de busqueda de la BD
    return {"Se encontro el usuario":id}