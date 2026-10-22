# EX021 — API de Tarefas com Testes Básicos

**Dificuldade:** Básico

## Contexto

Uma aplicação precisa de uma API para gerenciar tarefas. Antes de adicionar recursos mais complexos, é necessário garantir que seus endpoints funcionem corretamente por meio de testes automatizados.

A API deverá utilizar Pytest para verificar as respostas HTTP, os dados retornados e o comportamento dos endpoints.

## Objetivo

Introduzir os seguintes conceitos:

* Pytest e testes automatizados;
* Organização e execução de testes;
* `assert` para verificar resultados;
* `TestClient` do FastAPI;
* Testes de endpoints GET e POST;
* Verificação de códigos HTTP e respostas JSON;
* Testes de sucesso e de erro.

## Modelo

### Tarefa

* `id`
* `titulo`
* `descricao`
* `concluida`

> Utilize uma lista Python em memória para armazenar as tarefas, sem banco de dados neste exercício.

## Endpoints

```text
GET  /tarefas
GET  /tarefas/{id}
POST /tarefas
```

## Regras de negócio

### Tarefas

* O título é obrigatório.
* A descrição deve ser opcional.
* O campo `concluida` deve ser booleano e iniciar como `false`.
* A listagem deve retornar as tarefas cadastradas.
* A consulta deve retornar uma tarefa existente pelo seu ID.
* A consulta de uma tarefa inexistente deve retornar `404 Not Found`.
* O cadastro deve retornar `201 Created`.
* Os dados recebidos devem ser validados com Pydantic.
* Os testes devem verificar tanto os resultados esperados quanto os erros.

## Testes

* Crie arquivos de teste reconhecidos pelo Pytest.
* Utilize `TestClient` para realizar requisições à API.
* Verifique os códigos de status HTTP.
* Verifique os dados retornados em JSON.
* Teste o cadastro de uma tarefa válida.
* Teste a listagem de tarefas.
* Teste a consulta de uma tarefa existente e de uma inexistente.
* Teste o envio de dados inválidos.
* Garanta que os testes não dependam da execução manual da API.

## Organização

* Mantenha a aplicação FastAPI separada dos arquivos de teste.
* Utilize nomes de arquivos e funções reconhecidos pelo Pytest.
* Organize os testes em um diretório `tests/`.
* Utilize `pytest` para executar a suíte de testes.
* Instale as dependências necessárias para executar os testes.

## O que este exercício acrescenta

Até aqui, o foco foi construir APIs e implementar seus endpoints. Agora, o objetivo é aprender a verificar automaticamente se eles funcionam como esperado.

O principal desafio será entender como escrever testes que validem o comportamento da aplicação, identificando erros sem precisar verificar manualmente cada requisição.

**Não implemente banco de dados, autenticação, fixtures complexas ou testes de integração neste exercício.** Esses conceitos serão introduzidos progressivamente nos próximos exercícios.
