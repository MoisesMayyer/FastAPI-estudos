"""
EX008 — Analisador de números

Crie uma rota que receba uma lista de números e retorne
estatísticas completas: quantidade de números, maior valor,
menor valor, soma, média, quantidade de pares e quantidade de ímpares.
"""
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Analisador de numeros"}


@app.get("/analisador")
def rota(numeros: list[int] = Query()):

    quantidade_numeros = len(numeros)
    maior_numero = numeros[0]
    menor_numero = numeros[0]
    soma = 0
    quantidade_par = 0
    quantidade_impar = 0

    for c in range(quantidade_numeros):

        if maior_numero < numeros[c]:
            maior_numero = numeros[c]

        if menor_numero > numeros[c]:
            menor_numero = numeros[c]

        soma += numeros[c]

        if numeros[c] % 2 == 0:
            quantidade_par += 1
        else:
            quantidade_impar += 1

    media = soma / quantidade_numeros

    return {
        "quantidade de numeros": quantidade_numeros,
        "maior numero": maior_numero,
        "menor numero": menor_numero,
        "soma": soma,
        "quantidade_par": quantidade_par,
        "quantidade_impar": quantidade_impar,
        "media": media
    }

