import random

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/teste1")
async def funcaoteste():
    return {"teste": True, "Número aleatório": random.randint(0, 1000)}