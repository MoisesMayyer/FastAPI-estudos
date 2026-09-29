"""
EX001 — Saudação personalizada

Crie uma rota GET /ola/{nome} que receba um nome como Path Parameter
e retorne uma mensagem de saudação personalizada em formato JSON.

Exemplo de requisição: GET /ola/Moises
Resposta esperada: {"message": "Olá, Moises!"}
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Bem vindo!"}


@app.get("/ola/{nome}")
def ola(nome: str):
    return {"message": f"olá, {nome}!"}
