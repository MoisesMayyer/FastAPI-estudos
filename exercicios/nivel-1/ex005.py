"""
EX005 — Conversor de temperatura

Crie uma rota GET /converter que receba Query Parameters para o valor,
a unidade de origem e a unidade de destino, realizando a conversão
entre Celsius, Fahrenheit e Kelvin.
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "conversor de temperatura (use: K, F ou C)"}


@app.get("/converter")
def converter(valor:float, unidade_o:str, unidade_d:str):
    resultado = None

    if unidade_o == unidade_d:
        resultado = valor

    if unidade_o == "C" and unidade_d == "K":
        resultado = valor + 273.15

    elif unidade_o == "C" and unidade_d == "F":
        resultado = (valor * 1.8) + 32

    elif unidade_d == "F" and unidade_o == "K":
        resultado = (valor - 32) / 1.8 + 273.15

    elif unidade_d == "F" and unidade_o == "C":
        resultado = (valor - 32) / 1.8

    elif unidade_d == "K" and unidade_o == "C":
        resultado = valor - 273.15

    elif unidade_d == "K" and unidade_o == "F":
        resultado = (valor - 273.15) * 1.8 + 32

    else:
        return {"resultado": "digite unidades validas"}


    return {
        "valor": valor,
        "unidade_o": unidade_o,
        "unidade_d": unidade_d,
        "resultado": resultado
    }