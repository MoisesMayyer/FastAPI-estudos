# EX007 — API de Produtos com Autenticação e OAuth2

**Dificuldade:** Intermediário

## Contexto

Uma loja precisa de uma API para gerenciar produtos. Os usuários devem realizar login para acessar as funcionalidades protegidas, utilizando JWT para autenticação.

A API deverá diferenciar operações públicas de operações que exigem autenticação, aplicando regras de negócio para garantir a integridade dos produtos.

## Objetivo

Introduzir os seguintes conceitos:

* OAuth2 com `OAuth2PasswordBearer`;
* Fluxo de autenticação com JWT;
* `OAuth2PasswordRequestForm` para receber credenciais;
* Dependências para recuperar o usuário autenticado;
* Rotas públicas e protegidas;
* SQLAlchemy, PostgreSQL e Pydantic;
* CRUD e regras de negócio;
* Tratamento de erros HTTP.

## Modelos

### Produto

* `id`
* `nome`
* `descricao`
* `preco`
* `estoque`
* `ativo`

> Um produto novo deve começar como `ativo = true`.

> O preço deve ser maior que zero e o estoque não pode ser negativo.

### Usuario

Utilize o modelo de usuário desenvolvido no EX001, mantendo o armazenamento seguro das senhas.

## Endpoints

### Autenticação

```text
POST /auth/token
GET  /auth/me
```

### Produtos

```text
GET    /produtos
GET    /produtos/{id}
POST   /produtos
PUT    /produtos/{id}
DELETE /produtos/{id}
```

## Regras de negócio

### Autenticação

* O login deve validar as credenciais do usuário.
* O endpoint `/auth/token` deve receber os dados conforme o fluxo OAuth2 Password utilizado neste exercício.
* Após autenticação válida, deve retornar um JWT com prazo de expiração.
* Rotas protegidas devem validar o token recebido.
* Tokens inválidos ou expirados devem retornar `401 Unauthorized`.
* Usuários inativos não podem realizar login.
* O segredo JWT deve ser configurado por variável de ambiente.

### Produtos

* O nome é obrigatório.
* O preço deve ser maior que zero.
* O estoque não pode ser negativo.
* Não deve ser possível consultar, atualizar ou excluir um produto inexistente.
* Produtos inativos não devem ser tratados como disponíveis para operações que exijam um produto ativo.
* A listagem e a consulta de produtos devem ser públicas.
* O cadastro, a atualização e a exclusão devem exigir autenticação.
* Os dados recebidos devem ser validados com Pydantic.

## Organização

Utilize routers separados para `/auth` e `/produtos`.

Mantenha modelos SQLAlchemy, schemas Pydantic e lógica de segurança separados.

Utilize `Depends` para validar o token e recuperar o usuário autenticado.

## O que este exercício acrescenta

Nos exercícios anteriores, você implementou cadastro de usuários, verificação de senhas e autenticação com JWT.

Agora, deverá integrar esses conhecimentos ao fluxo OAuth2 do FastAPI, utilizando `OAuth2PasswordBearer` e `OAuth2PasswordRequestForm`.

Você também deverá decidir quais endpoints são públicos e quais exigem autenticação.

**Não implemente roles, refresh tokens ou rate limiting neste exercício.** Esses recursos serão trabalhados nos próximos exercícios.

> **Observação:** o fluxo OAuth2 Password é utilizado aqui para fins didáticos. Ele não é recomendado para novos sistemas de autenticação de usuários; o objetivo é compreender seu funcionamento e a integração com o FastAPI.