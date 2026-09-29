"""
EX004 — Média do aluno

Crie uma rota que receba o nome de um aluno e três notas como
Path Parameters, calcule a média aritmética e retorne os dados
completos incluindo a situação final do aluno (aprovado ou reprovado).
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "calculadora de medias"}


@app.get("/calcular_media/{nome}/{nota1}/{nota2}/{nota3}")
def calcular_media(nome: str, nota1: float, nota2: float, nota3: float):

    media = (nota1 + nota2 + nota3) /3
    if media >= 7:
        situacao ="aprovado"
    elif media >= 5:
        situacao ="recuperacao"
    else:
        situacao ="reprovado"

    return {
        "nome": nome,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
        "media": media,
        "situacao": situacao
    }
