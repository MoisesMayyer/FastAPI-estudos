# EX023 — API de Clientes com Testes de Banco de Dados

**Dificuldade:** Intermediário

## Contexto

Uma empresa precisa de uma API para gerenciar seus clientes. Além de validar os endpoints, será necessário garantir que as operações com o banco de dados funcionem corretamente e que os testes não afetem os dados utilizados durante o desenvolvimento.

A API deverá utilizar Pytest para testar as operações de CRUD com SQLAlchemy e PostgreSQL, mantendo o ambiente de testes isolado.

## Objetivo

Introduzir os seguintes conceitos:

* Testes com banco de dados;
* Fixtures para conexão e sessão;
* Isolamento dos dados de teste;
* Sobrescrita de dependências com `app.dependency_overrides`;
* Testes de integração com FastAPI e SQLAlchemy;
* Preparação e limpeza dos dados de teste;
* Verificação de operações de CRUD.

## Modelo

### Cliente

* `id`
* `nome`
* `email`
* `telefone`

> Utilize SQLAlchemy e PostgreSQL para persistir os clientes. Configure um banco de dados exclusivo para os testes.

## Endpoints

```text
GET    /clientes
GET    /clientes/{id}
POST   /clientes
PUT    /clientes/{id}
DELETE /clientes/{id}
```

## Regras de negócio

### Clientes

* O nome é obrigatório.
* O email deve ser válido.
* Não deve ser permitido cadastrar dois clientes com o mesmo email.
* A listagem deve retornar os clientes cadastrados.
* A consulta deve retornar um cliente existente pelo seu ID.
* A criação deve retornar `201 Created`.
* A atualização deve modificar os dados do cliente existente.
* A exclusão deve remover o cliente cadastrado.
* Operações sobre clientes inexistentes devem retornar `404 Not Found`.
* Os dados recebidos devem ser validados com Pydantic.

## Testes

* Crie fixtures para preparar a conexão e a sessão do banco de testes.
* Utilize `TestClient` para realizar requisições à API.
* Teste as operações de CRUD com persistência no banco.
* Verifique se os dados são salvos e consultados corretamente.
* Teste o cadastro de emails duplicados.
* Teste operações sobre clientes inexistentes.
* Garanta que os dados de um teste não interfiram em outros.
* Utilize `app.dependency_overrides` para substituir a dependência de banco da aplicação durante os testes.
* Garanta que a execução dos testes não modifique o banco de desenvolvimento.

## Organização

* Mantenha modelos SQLAlchemy, schemas Pydantic, configuração do banco e endpoints separados.
* Organize os testes no diretório `tests/`.
* Utilize fixtures para configurar e limpar o ambiente de testes.
* Mantenha a configuração do banco de testes separada da configuração de desenvolvimento.
* Execute a suíte utilizando `pytest`.

## O que este exercício acrescenta

Nos exercícios anteriores, você aprendeu a testar endpoints, validar respostas e reutilizar dados com fixtures.

Agora, deverá aplicar esses conhecimentos a uma API com persistência real, garantindo que os testes verifiquem o comportamento integrado entre FastAPI e SQLAlchemy.

O principal desafio será **isolar o ambiente de testes**, evitando que os testes dependam uns dos outros ou alterem os dados da aplicação durante o desenvolvimento.

**Não implemente autenticação, JWT ou permissões de usuários neste exercício.** Esses conceitos serão trabalhados no próximo exercício.
