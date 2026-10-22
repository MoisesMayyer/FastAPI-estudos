# EX022 — API de Produtos com Fixtures e Validação

**Dificuldade:** Básico+

## Contexto

Uma loja precisa de uma API para gerenciar seus produtos. Para garantir que os endpoints funcionem corretamente, será necessário ampliar os testes automatizados, reutilizando dados e configurações entre diferentes testes.

A API deverá utilizar Pytest para testar as operações de CRUD, validar dados recebidos e verificar respostas de sucesso e erro.

## Objetivo

Introduzir os seguintes conceitos:

* Fixtures com `@pytest.fixture`;
* Reutilização de dados e configurações de teste;
* Testes de CRUD;
* Validação de dados com Pydantic;
* Testes de respostas HTTP;
* Testes de erros e entradas inválidas;
* Organização dos testes em múltiplos arquivos.

## Modelo

### Produto

* `id`
* `nome`
* `descricao`
* `preco`
* `disponivel`

> Utilize uma lista Python em memória para armazenar os produtos, sem banco de dados neste exercício.

## Endpoints

```text
GET    /produtos
GET    /produtos/{id}
POST   /produtos
PUT    /produtos/{id}
DELETE /produtos/{id}
```

## Regras de negócio

### Produtos

* O nome é obrigatório.
* O preço deve ser maior que zero.
* A descrição deve ser opcional.
* O campo `disponivel` deve ser booleano e iniciar como `true`.
* A listagem deve retornar os produtos cadastrados.
* A consulta deve retornar um produto existente pelo seu ID.
* A criação deve retornar `201 Created`.
* A atualização deve modificar os dados do produto existente.
* A exclusão deve remover o produto cadastrado.
* Operações sobre produtos inexistentes devem retornar `404 Not Found`.
* Os dados recebidos devem ser validados com Pydantic.

## Testes

* Crie fixtures para preparar dados reutilizáveis.
* Utilize `TestClient` para testar os endpoints.
* Teste as operações de criação, consulta, atualização e exclusão.
* Verifique os códigos de status HTTP e os dados retornados em JSON.
* Teste preços inválidos e campos obrigatórios ausentes.
* Teste operações sobre produtos inexistentes.
* Garanta que os testes não dependam da ordem de execução.
* Utilize fixtures para evitar repetição desnecessária nos testes.

## Organização

* Mantenha a aplicação FastAPI separada dos arquivos de teste.
* Organize os testes no diretório `tests/`.
* Separe os testes por responsabilidade, quando necessário.
* Utilize nomes de arquivos e funções reconhecidos pelo Pytest.
* Execute a suíte utilizando `pytest`.

## O que este exercício acrescenta

No exercício anterior, você aprendeu a escrever testes básicos para endpoints e verificar suas respostas.

Agora, deverá aprender a reutilizar configurações e dados com fixtures, reduzindo a repetição e facilitando a manutenção dos testes.

O principal desafio será garantir que cada teste valide o comportamento esperado sem depender dos resultados ou da ordem de execução de outros testes.

**Não implemente banco de dados, autenticação ou testes de integração neste exercício.** Esses conceitos serão introduzidos nos próximos exercícios.
