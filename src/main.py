import random

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Estudante(BaseModel):
    name: str
    curso: str
    ativo: bool

#127.0.00.1:8000/
@app.get("/")
async def root():
    return {"message": "Hello World"}

#127.0.00.1:8000/teste
@app.get("/teste")
async def funcaoteste():
    return {"teste": True, "Número aleatório": random.randint(0, 20000)}

@app.post("/estudantes/cadastro")
async def create_estudante(estudante: Estudante):
    return estudante

@app.put("/estudantes/update/{id_estudante}")
async def update_estudante(id_estudante: int):
    return id_estudante > 0

@app.delete("/estudantes/delete/{id_estudante}")
async def delete_estudante(id_estudante: int):
    return id_estudante > 0
