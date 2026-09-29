"""
EX009 — Boletim escolar

Crie uma rota que receba o nome de um aluno e várias notas,
calcule a média, a maior e a menor nota, a quantidade de notas
acima da média e a situação final (aprovado, recuperação ou reprovado).
"""
from fastapi import FastAPI, Query


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Boletim escolar"}


@app.get("/boletim")
def notas(nome: str, notas_prova: list[float] = Query()):

    qtd_notas = len(notas_prova)
    soma = 0

    maior_nota = notas_prova[0]
    menor_nota = notas_prova[0]

    qtd_acima_media = 0

    for i in range(qtd_notas):

        if maior_nota < notas_prova[i]:
            maior_nota = notas_prova[i]

        if menor_nota > notas_prova[i]:
            menor_nota = notas_prova[i]

        soma += notas_prova[i]

    media = soma / qtd_notas

    if media >= 6:
        resultado = "aprovado"
    elif media >= 5:
        resultado = "recuperacao"
    else:
        resultado = "reprovado"

    for i in range(qtd_notas):
        if notas_prova[i] > media:
            qtd_acima_media += 1


    return {
        "nome": nome,
        "notas": notas_prova,
        "quantidade de notas": qtd_notas,
        "maior nota": maior_nota,
        "menor nota": menor_nota,
        "media": media,
        "acima nota": qtd_acima_media,
        "resultado": resultado
    }
