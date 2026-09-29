"""
EX007 — Tabuada

Crie uma rota GET /tabuada/{numero} que receba um número como
Path Parameter e um limite como Query Parameter, retornando a
tabuada completa do número informado até o limite estabelecido.
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Tabuada"}


@app.get("/tabuada/{valor}")
def tabuada(valor:int, limite: int =10):

    tabuadas = []

    for contador in range(1, limite + 1):

        valor_tabuada = contador * valor

        tabuadas.append(valor_tabuada)


    return tabuadas