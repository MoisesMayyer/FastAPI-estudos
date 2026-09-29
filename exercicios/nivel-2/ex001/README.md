# EX001 — Cadastro de produtos

**Dificuldade:** Fácil

## Contexto

Você deve construir uma API REST para controlar os produtos de uma pequena loja.

A aplicação deve permitir cadastrar, consultar, atualizar e remover produtos. Os dados devem ser persistidos em um banco de dados utilizando SQLAlchemy.

## Objetivo

Praticar o fluxo básico de uma aplicação FastAPI utilizando:

- APIRouter;
- organização das rotas em arquivo separado;
- métodos HTTP;
- SQLAlchemy;
- modelo de banco de dados;
- operações básicas de CRUD;
- respostas JSON;
- documentação automática em /docs.

## Modelo Produto

Cada produto deve possuir:

- id
- nome
- preco
- estoque
- ativo

Sugestão de tipos:

| Campo    | Tipo             |
|----------|------------------|
| id       | inteiro          |
| nome     | texto            |
| preco    | número decimal   |
| estoque  | inteiro          |
| ativo    | booleano         |

> `ativo` deve possuir valor padrão `true`.

## Endpoints

Implemente:

```
GET    /produtos
GET    /produtos/{id}
POST   /produtos
PUT    /produtos/{id}
DELETE /produtos/{id}
```

## Regras de negócio

- O nome do produto é obrigatório.
- O preço deve ser maior que 0.
- O estoque não pode ser negativo.
- Ao criar um produto, ele deve começar como ativo.
- Não deve ser possível consultar, atualizar ou excluir um produto que não existe. Nesse caso, a API deve retornar 404.
- Ao excluir um produto existente, ele deve deixar de ser retornado pelas consultas.

## O que não será exigido

Não haverá relacionamentos entre tabelas nem regras complexas de estoque.

A ideia aqui é você dominar o fluxo:

```
Router → SQLAlchemy → Banco → Resposta
```