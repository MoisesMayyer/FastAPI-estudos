"""
EX002 — Calculadora

Crie uma rota GET /calcular/{numero1}/{numero2} que receba dois números
inteiros como Path Parameters e retorne o resultado de quatro operações
matemáticas: soma, subtração, multiplicação e divisão.

Exemplo de requisição: GET /calcular/10/2
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "bem vindo a calculadora"}


@app.get("/calcular/{numero1}/{numero2}")
def calcular(numero1: int, numero2: int):

    if numero2 == 0:
        divisao = "Não é possível dividir por zero"
    else:
        divisao = numero1 / numero2

    return {
        "soma": numero1 + numero2,
        "subtracao": numero1 - numero2,
        "multiplicacao": numero1 * numero2,
        "divisao": divisao
    }
