# EX002 — API de Tarefas com JWT

**Dificuldade:** Intermediário

## Contexto

Uma plataforma precisa de uma API para gerenciar tarefas pessoais. Os usuários devem realizar login e receber um token JWT para acessar as funcionalidades protegidas.

Cada tarefa deve pertencer a um usuário, impedindo que ele consulte ou altere tarefas de outras pessoas.

## Objetivo

Introduzir os seguintes conceitos:

- Autenticação com JWT;
- OAuth2 com `OAuth2PasswordBearer`;
- Criação e validação de tokens;
- `Depends` para proteger endpoints;
- Identificação do usuário autenticado;
- Relacionamentos com `ForeignKey`;
- Pydantic, SQLAlchemy e PostgreSQL;
- Regras de negócio e tratamento de erros HTTP.

## Modelos

### Tarefa

- `id`
- `titulo`
- `descricao`
- `concluida`
- `usuario_id`

> `usuario_id` deve ser uma chave estrangeira para o usuário proprietário da tarefa.

> Uma tarefa nova deve começar como `concluida = false`.

> Utilize o modelo de usuário e o sistema de hash de senhas do **EX005**.

## Endpoints

### Autenticação

| Método | Rota | Descrição |
|--------|------|-----------|
| `POST` | `/auth/login` | Login e obtenção do token JWT |
| `GET`  | `/auth/me`    | Dados do usuário autenticado |

### Tarefas

| Método | Rota | Descrição |
|--------|------|-----------|
| `GET`    | `/tarefas`       | Listar tarefas do usuário |
| `GET`    | `/tarefas/{id}`  | Consultar tarefa específica |
| `POST`   | `/tarefas`       | Criar nova tarefa |
| `PUT`    | `/tarefas/{id}`  | Atualizar tarefa |
| `DELETE` | `/tarefas/{id}`  | Excluir tarefa |

## Regras de negócio

### Autenticação

- O login deve validar as credenciais do usuário.
- Após um login válido, a API deve gerar um JWT com prazo de expiração.
- O token deve identificar o usuário autenticado.
- Tokens inválidos ou expirados devem retornar `401 Unauthorized`.
- Usuários inativos não podem realizar login.
- O segredo utilizado para assinar o token deve ser configurado por variável de ambiente.

### Tarefas

- O título é obrigatório.
- Uma tarefa deve pertencer a um usuário existente.
- Todas as operações devem exigir autenticação.
- O usuário só pode listar, consultar, atualizar e excluir suas próprias tarefas.
- Não deve ser possível consultar ou alterar uma tarefa inexistente ou pertencente a outro usuário.
- Uma tarefa nova deve começar como não concluída.
- O cliente não pode definir livremente o `usuario_id` para assumir a propriedade de tarefas de outro usuário.

## Organização

- Utilize routers separados para `/auth` e `/tarefas`.
- Mantenha a separação entre modelos SQLAlchemy, schemas Pydantic e lógica de segurança.
- Crie uma dependency utilizando `Depends` para recuperar o usuário autenticado a partir do JWT validado.

## O que este exercício acrescenta

No **EX005**, o login apenas verificava as credenciais. Agora, ele deverá gerar um token que será enviado nas próximas requisições.

Você precisará validar esse token e identificar o usuário responsável por cada operação.

> **Não implemente** refresh tokens, roles, permissões administrativas ou rate limiting neste exercício. Esses conceitos serão introduzidos gradualmente nos próximos exercícios.