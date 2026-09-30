# EX003 — Usuários e Tarefas

**Dificuldade:** Fácil

## Contexto

Uma aplicação precisa de uma API para controlar usuários e as tarefas que eles possuem.

Um usuário pode possuir várias tarefas, mas cada tarefa pertence a um único usuário.

## Objetivo

Aumentar a complexidade do exercício anterior introduzindo:

* duas tabelas;
* ForeignKey;
* relacionamento entre entidades;
* CRUD de mais de um recurso;
* Pydantic para validação dos dados recebidos;
* `Depends` para gerenciamento da sessão do banco;
* `yield` para garantir o fechamento da sessão;
* armazenamento seguro das senhas utilizando hash;
* organização dos endpoints utilizando routers.

## Modelos

### Usuário

* id
* nome
* email
* senha

### Tarefa

* id
* titulo
* descricao
* concluida
* usuario_id

> `usuario_id` deve ser uma chave estrangeira para Usuário.

> `concluida` deve começar como `false`.

> A senha não deve ser armazenada em texto puro. Deve ser armazenado apenas o seu hash.

## Endpoints

### Usuários

```text
GET    /usuarios
GET    /usuarios/{id}
POST   /usuarios
PUT    /usuarios/{id}
DELETE /usuarios/{id}
```

### Tarefas

```text
GET    /tarefas
GET    /tarefas/{id}
POST   /tarefas
PUT    /tarefas/{id}
DELETE /tarefas/{id}
```

## Regras de negócio

* O nome do usuário é obrigatório.
* O email do usuário é obrigatório.
* A senha do usuário é obrigatória no cadastro.
* A senha não deve ser armazenada diretamente no banco de dados.
* O título da tarefa é obrigatório.
* A descrição da tarefa pode ser opcional.
* Uma tarefa deve obrigatoriamente estar associada a um usuário existente.
* Não é permitido cadastrar uma tarefa apontando para um `usuario_id` inexistente.
* Uma tarefa nova deve começar como não concluída.
* Não deve ser possível consultar, atualizar ou excluir um registro inexistente.
* Um usuário não deve ser excluído enquanto possuir tarefas associadas.
* A sessão do banco deve ser criada através de uma dependency.
* A sessão deve ser fechada corretamente após o término da requisição.

## Organização

Utilize routers para separar os endpoints de usuários e tarefas.

A sessão do banco de dados deve ser disponibilizada através de uma dependency utilizando `Depends` e `yield`.

Utilize schemas com Pydantic para definir e validar os dados recebidos pela API.

## O que este exercício acrescenta

No EX002 você começou a trabalhar com relacionamentos entre tabelas.

Agora você continuará trabalhando com esse conceito, mas adicionará algumas responsabilidades novas.

Antes, você poderia receber os dados diretamente na função da rota.

Agora deverá pensar:

> "Quais dados minha API aceita?"

E utilizar um schema Pydantic para definir isso.

Também deverá pensar:

> "Quem cria e fecha a sessão do banco?"

Em vez de criar e fechar a sessão manualmente em cada rota, você deverá utilizar uma dependency com `Depends` e `yield`.

Por fim, você terá uma informação sensível:

> "Como armazenar a senha do usuário?"

A senha não deve ser salva diretamente. Você deverá gerar um hash antes de armazená-la.

O exercício ainda não exige sistema de login ou JWT. O objetivo é praticar os conceitos aprendidos até esta aula sem aumentar demais a complexidade.
