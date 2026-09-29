"""
EX010 — Sistema de compra

Crie uma rota que receba produto, preço, quantidade e forma de pagamento,
calcule o valor total aplicando regras de desconto ou acréscimo conforme
a forma de pagamento, retornando um resumo completo da compra.
"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "sistema de compra"}


@app.get("/compra")
def compra(produto: str = '',preco: float = 0, quantidade: int = 0, forma_pagamento: str = 'dinheiro'):

    desconto = 0
    valor_final = 0
    acrescimo = 0

    sub_total = quantidade * preco

    if forma_pagamento == 'dinheiro':
        porcentagem_desconto = 0.05
        desconto = sub_total * porcentagem_desconto
        valor_final = sub_total - desconto

    elif forma_pagamento == 'pix':
        porcentagem_desconto = 0.15
        desconto = sub_total * porcentagem_desconto
        valor_final = sub_total - desconto

    elif forma_pagamento == 'cartao':
        valor_final = sub_total - desconto

    elif forma_pagamento == 'parcelado':
        porcentagem_acrescimo = 0.15
        acrescimo = sub_total * porcentagem_acrescimo
        valor_final = sub_total + acrescimo
    else:
        return {"message": "formas de pagamentos aceitas: pix, cartao, parcelado e dinheiro"}

    return {
        "produto": produto,
        "quantidade": quantidade,
        "subtotal": sub_total,
        "desconto": desconto,
        "acrescimo": acrescimo,
        "total": valor_final
    }