# EX004 — Sistema de Academia

**Dificuldade:** Intermediário

## Contexto

Uma academia precisa de uma API para controlar seus alunos, planos e matrículas.

Cada aluno pode possuir matrículas em planos, e cada matrícula pertence a um único aluno e a um único plano.

A API deve permitir o cadastro e gerenciamento dos alunos, planos e matrículas, além de aplicar algumas regras de negócio para impedir operações inválidas.

## Objetivo

Aumentar a complexidade do exercício anterior introduzindo:

* três tabelas;
* múltiplos relacionamentos entre entidades;
* ForeignKey;
* CRUD de três recursos;
* Pydantic para validação dos dados;
* `Depends` para gerenciamento da sessão do banco;
* `yield` para garantir o fechamento da sessão;
* hash de senha;
* validação da existência de registros relacionados;
* regras de negócio envolvendo mais de uma tabela;
* organização dos endpoints utilizando routers.

## Modelos

### Aluno

* id
* nome
* email
* senha
* ativo

### Plano

* id
* nome
* preco
* duracao_dias
* ativo

### Matricula

* id
* aluno_id
* plano_id
* data_inicio
* data_fim
* ativa

> `aluno_id` deve ser uma chave estrangeira para Aluno.

> `plano_id` deve ser uma chave estrangeira para Plano.

> Um aluno pode possuir várias matrículas ao longo do tempo.

> Uma matrícula pertence a apenas um aluno e um plano.

> A senha do aluno não deve ser armazenada em texto puro. Deve ser armazenado apenas o seu hash.

> Um aluno novo deve começar como `ativo = true`.

> Um plano novo deve começar como `ativo = true`.

> Uma matrícula nova deve começar como `ativa = true`.

## Relacionamentos

```text
Aluno
  │
  └────< Matricula >────┐
                        │
                      Plano
```

Um aluno pode possuir várias matrículas.

Um plano pode estar associado a várias matrículas.

Uma matrícula pertence a um único aluno e a um único plano.

## Endpoints

### Alunos

```text
GET    /alunos
GET    /alunos/{id}
POST   /alunos
PUT    /alunos/{id}
DELETE /alunos/{id}
```

### Planos

```text
GET    /planos
GET    /planos/{id}
POST   /planos
PUT    /planos/{id}
DELETE /planos/{id}
```

### Matrículas

```text
GET    /matriculas
GET    /matriculas/{id}
POST   /matriculas
PUT    /matriculas/{id}
DELETE /matriculas/{id}
```

## Regras de negócio

### Alunos

* O nome do aluno é obrigatório.
* O email é obrigatório.
* A senha é obrigatória no cadastro.
* O email de dois alunos não pode ser igual.
* A senha deve ser armazenada utilizando hash.
* Um aluno novo deve começar como ativo.
* Não deve ser possível consultar, atualizar ou excluir um aluno inexistente.
* Um aluno que possua uma matrícula ativa não pode ser excluído.
* Um aluno inativo não pode receber uma nova matrícula.

### Planos

* O nome do plano é obrigatório.
* O preço deve ser maior que `0`.
* A duração deve ser maior que `0`.
* Dois planos não devem possuir o mesmo nome.
* Um plano novo deve começar como ativo.
* Não deve ser possível consultar, atualizar ou excluir um plano inexistente.
* Um plano que possua matrículas ativas não pode ser excluído.
* Um plano inativo não pode receber novas matrículas.

### Matrículas

* O aluno informado deve existir.
* O plano informado deve existir.
* O aluno precisa estar ativo.
* O plano precisa estar ativo.
* `data_inicio` é obrigatória.
* `data_fim` deve ser posterior à `data_inicio`.
* Uma matrícula nova deve começar como ativa.
* Um aluno não pode possuir duas matrículas ativas ao mesmo tempo.
* Não deve ser possível criar uma matrícula para um aluno inexistente.
* Não deve ser possível criar uma matrícula para um plano inexistente.
* Não deve ser possível consultar, atualizar ou excluir uma matrícula inexistente.
* Ao cancelar uma matrícula, ela deve deixar de ser considerada ativa.

## Regras adicionais

Ao atualizar um aluno ou plano, deve ser possível alterar seus dados normalmente, mas as regras de negócio continuam sendo aplicadas.

Por exemplo:

> Um plano que possui matrículas ativas não pode ser desativado de maneira que permita uma nova matrícula.

Uma matrícula também não deve poder ser alterada para apontar para um aluno ou plano inexistente.

As operações que envolvem relacionamentos devem verificar a existência dos registros antes de realizar alterações no banco.

## Organização

Utilize routers separados para:

```text
/alunos
/planos
/matriculas
```

Utilize schemas Pydantic para definir os dados recebidos pela API.

A sessão do banco deve ser disponibilizada através de uma dependency utilizando `Depends` e `yield`.

Utilize `HTTPException` para retornar erros apropriados quando uma regra de negócio for violada.

## O que este exercício acrescenta

No EX003 você trabalhava principalmente com:

> "Esse usuário existe?"

Agora você terá que lidar com relações entre três entidades.

Ao criar uma matrícula, por exemplo, você precisará verificar:

> "O aluno existe?"

> "O plano existe?"

> "O aluno está ativo?"

> "O plano está ativo?"

> "Esse aluno já possui uma matrícula ativa?"

Além disso, algumas operações agora dependem do estado de outras tabelas.

Por exemplo:

> "Posso excluir este plano?"

Para responder, você precisará verificar se existem matrículas ativas relacionadas a ele.

O exercício continua utilizando os mesmos conceitos aprendidos até agora, mas exige mais raciocínio para implementar as regras de negócio e manter a integridade dos dados.

Não é necessário implementar login, JWT, autorização ou outras funcionalidades de autenticação neste exercício. O hash da senha é suficiente para continuar praticando o conteúdo aprendido na aula.
