"""
EX006 — Calculadora de desconto

Crie uma rota que receba o preço e o percentual de desconto,
calcule o valor do desconto e o preço final.
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Calculadora de desconto. Informe o valor e o desconto a ser aplicado."}


@app.get("/calculadora")
def calculadora_desconto(valor: float, percentual_desconto: int):

    if valor <= 0:
        return {"message": "Valor invalido, somente valores positivos."}

    if percentual_desconto < 0:
        return {"message": "descontos menores que zero nao sao permitidos."}
    elif percentual_desconto > 100:
        return {"message": "descontos superiores a 100% nao sao permitidos"}

    valor_desconto = percentual_desconto / 100
    calculo_desconto = valor *  valor_desconto
    preco_final = valor - calculo_desconto

    return {
        "valor_inicial": valor,
        "percentual_desconto": percentual_desconto,
        "valor_desconto": calculo_desconto,
        "preco_final": preco_final,
    }