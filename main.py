import random

from fastapi import FastAPI

app = FastAPI()

#127.0.00.1:8000/
@app.get("/")
async def root():
    return {"message": "Hello World"}

#127.0.00.1:8000/teste
@app.get("/teste")
async def funcaoteste():
    return {"teste": True, "Número aleatório": random.randint(0, 20000)}