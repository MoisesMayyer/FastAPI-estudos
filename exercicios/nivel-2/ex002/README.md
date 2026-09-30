# EX002 — Biblioteca

**Dificuldade:** Fácil

## Contexto

Uma biblioteca precisa de uma API para controlar seus livros e autores.

Um autor pode possuir vários livros, mas cada livro pertence a um único autor.

## Objetivo

Aumentar a complexidade do exercício anterior introduzindo:

- duas tabelas;
- ForeignKey;
- relacionamento entre entidades;
- CRUD de mais de um recurso;
- validação da existência de registros relacionados;
- organização dos endpoints utilizando routers.

## Modelos

### Autor

- id
- nome
- email

### Livro

- id
- titulo
- ano_publicacao
- disponivel
- autor_id

> `autor_id` deve ser uma chave estrangeira para Autor.

> `disponivel` deve começar como `true`.

## Endpoints

### Autores

```
GET    /autores
GET    /autores/{id}
POST   /autores
PUT    /autores/{id}
DELETE /autores/{id}
```

### Livros

```
GET    /livros
GET    /livros/{id}
POST   /livros
PUT    /livros/{id}
DELETE /livros/{id}
```

## Regras de negócio

- O nome do autor é obrigatório.
- O título do livro é obrigatório.
- O ano de publicação não pode ser inválido.
- Um livro deve obrigatoriamente estar associado a um autor existente.
- Não é permitido cadastrar um livro apontando para um autor_id inexistente.
- Não deve ser possível consultar, atualizar ou excluir um registro inexistente.
- Um livro novo deve começar como disponível.
- Um autor não deve ser excluído enquanto possuir livros associados.

Essa última regra é importante porque agora a operação de exclusão precisa considerar o relacionamento entre as tabelas.

## O que este exercício acrescenta

No EX001 você perguntava:

> "Esse produto existe?"

Agora você também precisa pensar:

> "O autor informado existe?"

E:

> "Posso remover esse autor sem quebrar a relação existente?"

Ainda é um exercício simples, mas já começa a exigir raciocínio sobre banco de dados.

---