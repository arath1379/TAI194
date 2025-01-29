from fastapi import FastAPI

app= FastAPI()

#ruta o ENDPOINT
@app.get('/')
def home():
    return {'hello': 'world fastApi'}