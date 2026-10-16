# EX019 — API de Gestão de Projetos com Autenticação e JWT

**Dificuldade:** Intermediário+

## Contexto

Uma equipe precisa de uma API para gerenciar projetos e suas tarefas. Cada usuário deve acessar apenas os projetos que criou, garantindo que não possa consultar, atualizar ou excluir recursos de outros usuários.

A API deverá utilizar JWT para autenticação e aplicar regras de autorização para proteger os dados.

## Objetivo

Introduzir os seguintes conceitos:

* OAuth2 com `OAuth2PasswordBearer`;
* Autenticação com JWT;
* `OAuth2PasswordRequestForm` para receber credenciais;
* Dependências para recuperar o usuário autenticado;
* Autorização baseada na propriedade dos recursos;
* Relacionamentos entre usuários, projetos e tarefas;
* SQLAlchemy, PostgreSQL e Pydantic;
* CRUD e regras de negócio;
* Tratamento de erros HTTP.

## Modelos

### Projeto

* `id`
* `nome`
* `descricao`
* `usuario_id`

> Todo projeto deve estar vinculado ao usuário que o criou.

### Tarefa

* `id`
* `titulo`
* `descricao`
* `concluida`
* `projeto_id`

> Uma tarefa deve pertencer a um projeto existente.

### Usuario

Utilize o modelo de usuário desenvolvido nos exercícios anteriores, mantendo o armazenamento seguro das senhas e os campos necessários para autenticação.

## Endpoints

### Autenticação

```text
POST /auth/token
GET  /auth/me
```

### Projetos

```text
GET    /projetos
GET    /projetos/{id}
POST   /projetos
PUT    /projetos/{id}
DELETE /projetos/{id}
```

### Tarefas

```text
GET    /projetos/{projeto_id}/tarefas
POST   /projetos/{projeto_id}/tarefas
PUT    /tarefas/{id}
DELETE /tarefas/{id}
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

### Projetos

* O nome é obrigatório.
* Todo projeto deve pertencer ao usuário autenticado.
* A listagem deve retornar apenas os projetos do próprio usuário.
* Não deve ser possível consultar, atualizar ou excluir projetos de outros usuários.
* Não deve ser possível consultar, atualizar ou excluir um projeto inexistente.
* O `usuario_id` deve ser obtido do usuário autenticado, não dos dados enviados pelo cliente.
* A exclusão de um projeto deve tratar corretamente suas tarefas relacionadas.

### Tarefas

* O título é obrigatório.
* Toda tarefa deve estar vinculada a um projeto existente.
* O usuário só pode listar, cadastrar, atualizar ou excluir tarefas de projetos aos quais tem acesso.
* Não deve ser possível atualizar ou excluir uma tarefa inexistente.
* O campo `concluida` deve ser booleano.
* Os dados recebidos devem ser validados com Pydantic.

## Organização

* Utilize routers separados para `/auth`, `/projetos` e `/tarefas`.
* Mantenha modelos SQLAlchemy, schemas Pydantic, configuração do banco e lógica de segurança separados.
* Utilize `Depends` para validar o token e recuperar o usuário autenticado.
* Utilize relacionamentos SQLAlchemy para representar as relações entre usuários, projetos e tarefas.

## O que este exercício acrescenta

Nos exercícios anteriores, você implementou cadastro de usuários, verificação de senhas e autenticação com JWT.

Agora, deverá integrar esses conhecimentos a uma API com múltiplos recursos relacionados, aplicando autorização baseada na propriedade dos dados.

O principal desafio será garantir que a **autenticação não seja confundida com autorização**: estar autenticado não significa ter permissão para acessar qualquer projeto ou tarefa.

**Não implemente roles, permissões administrativas, refresh tokens ou rate limiting neste exercício.** Esses recursos serão trabalhados nos próximos exercícios.

> **Observação:** o fluxo OAuth2 Password é utilizado aqui para fins didáticos. Ele não é recomendado para novos sistemas de autenticação de usuários; o objetivo é compreender seu funcionamento e a integração com o FastAPI.
