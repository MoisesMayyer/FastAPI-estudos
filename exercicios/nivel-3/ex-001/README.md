# EX001 — Sistema de Cadastro e Autenticação

**Dificuldade:** Intermediário

## Contexto

Uma plataforma precisa de uma API para cadastrar e gerenciar usuários, permitindo criar contas e autenticar credenciais por meio de e-mail e senha.

A API deve armazenar as senhas com segurança e aplicar regras de negócio para impedir operações inválidas.

## Objetivo

Introduzir os seguintes conceitos:

* CRUD de usuários;
* SQLAlchemy e PostgreSQL;
* Pydantic para validação;
* `Depends` e `yield` para gerenciamento da sessão;
* Hash e verificação de senhas;
* Autenticação por e-mail e senha;
* Routers e tratamento de erros HTTP.

## Modelo

### Usuario

* id
* nome
* email
* senha_hash
* ativo

> A senha deve ser armazenada como hash, nunca em texto puro.

> Um usuário novo deve começar como `ativo = true`.

## Endpoints

```text
GET    /usuarios
GET    /usuarios/{id}
POST   /usuarios
PUT    /usuarios/{id}
DELETE /usuarios/{id}

POST   /auth/login
```

## Regras de negócio

### Usuários

* Nome e e-mail são obrigatórios.
* O e-mail deve ser válido e único.
* A senha deve possuir no mínimo 8 caracteres.
* A senha deve ser armazenada utilizando hash seguro, como Argon2id ou bcrypt.
* Não deve ser possível consultar, atualizar ou excluir um usuário inexistente.
* Não deve ser permitido alterar o ID ou o hash da senha diretamente.
* As respostas não podem expor a senha ou seu hash.

### Autenticação

* O login deve receber e-mail e senha.
* As credenciais devem ser verificadas corretamente.
* Usuários inativos não podem realizar login.
* Credenciais inválidas devem retornar `401 Unauthorized`.
* O login não deve revelar se o e-mail ou a senha estão incorretos.
* Não deve ser gerado JWT neste exercício.

## Organização

Utilize routers separados para `/usuarios` e `/auth`.

Organize o projeto em módulos, separando:

```text
main.py
database.py
models.py
schemas.py
security.py
routers/
```

Utilize schemas Pydantic distintos para cadastro, atualização e resposta.

A sessão do banco deve ser gerenciada por uma dependency utilizando `Depends` e `yield`.

## O que este exercício acrescenta

Além do CRUD, você deverá implementar o armazenamento seguro de senhas e a verificação de credenciais.

Ao cadastrar um usuário, será necessário verificar se o e-mail já existe e gerar o hash da senha.

No login, será necessário verificar as credenciais e confirmar que a conta está ativa.

**Não implemente JWT, refresh tokens, permissões ou rate limiting neste exercício.** Esses conceitos serão abordados nos próximos exercícios.