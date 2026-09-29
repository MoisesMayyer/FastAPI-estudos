"""
EX003 — Analisador de número

Crie uma rota GET /analisar/{valor} que receba um número inteiro
como Path Parameter e retorne informações sobre ele: se é positivo,
negativo ou zero; se é par ou ímpar; seu dobro e seu quadrado.
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "analisador de numero"}


@app.get("/analisar/{valor}")
def analisar(valor: int):
    tipo = None

    if valor > 0:
        tipo = "positivo"
    elif valor < 0:
        tipo = "negativo"
    else:
        tipo = "zero"

    if valor % 2 == 0:
        impar_ou_par = "par"
    else:
        impar_ou_par = "impar"

    dobro = valor * 2
    quadrado = valor * valor

    return {
        "tipo": tipo,
        "valor": valor,
        "paridade": impar_ou_par,
        "dobro": dobro,
        "quadrado": quadrado,
    }
