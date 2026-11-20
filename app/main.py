from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="PC3 - API FastAPI")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/sumar")
def sumar(a: int, b: int):
    return {"resultado": a + b}


class Numeros(BaseModel):
    valores: List[float]

# promedio
@app.post("/promedio")
def promedio(datos: Numeros):
    if not datos.valores:
        raise HTTPException(status_code=400, detail="lista vacía")
    return {"promedio": sum(datos.valores) / len(datos.valores)}
