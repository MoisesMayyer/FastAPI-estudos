# EX020 — API de Administração com RBAC e Refresh Tokens

**Dificuldade:** Avançado

## Contexto

Uma empresa precisa de uma API para gerenciar usuários e controlar o acesso às funcionalidades do sistema. Cada usuário possui uma função que determina suas permissões.

A API deverá utilizar JWT para autenticação, refresh tokens para renovação de sessões e RBAC para controlar o acesso aos endpoints administrativos.

## Objetivo

Introduzir os seguintes conceitos:

* OAuth2 com `OAuth2PasswordBearer`;
* Autenticação com JWT e access tokens;
* Refresh tokens e renovação de sessões;
* Rotação e revogação de refresh tokens;
* RBAC (*Role-Based Access Control*);
* Dependências reutilizáveis para controle de permissões;
* SQLAlchemy, PostgreSQL e Pydantic;
* Gerenciamento de usuários e sessões;
* Tratamento de erros HTTP.

## Modelos

### Usuario

* `id`
* `nome`
* `email`
* `senha`
* `role`
* `ativo`

> A senha deve ser armazenada utilizando hash. O campo `role` deve aceitar apenas as funções permitidas pelo sistema.

### RefreshToken

* `id`
* `usuario_id`
* `token_hash`
* `expira_em`
* `revogado`

> Armazene o hash do refresh token, não o token original. Cada token deve estar vinculado a um usuário e possuir prazo de validade.

## Endpoints

### Autenticação

```text
POST  /auth/token
POST  /auth/refresh
POST  /auth/logout
GET   /auth/me
PATCH /auth/change-password
```

### Usuários

```text
GET   /usuarios
GET   /usuarios/{id}
PATCH /usuarios/{id}/role
PATCH /usuarios/{id}/status
```

## Regras de negócio

### Autenticação

* O login deve validar as credenciais do usuário.
* O endpoint `/auth/token` deve receber as credenciais conforme o fluxo OAuth2 Password utilizado neste exercício.
* Após autenticação válida, deve retornar um access token e um refresh token.
* O access token deve possuir um prazo de expiração curto.
* O refresh token deve possuir um prazo de expiração maior que o access token.
* Tokens inválidos ou expirados devem retornar `401 Unauthorized`.
* Usuários inativos não podem realizar login nem acessar endpoints protegidos.
* O segredo JWT deve ser configurado por variável de ambiente.

### Refresh tokens

* O endpoint `/auth/refresh` deve validar o refresh token recebido.
* O refresh token deve ser verificado no banco por meio do seu hash.
* Um refresh token expirado, revogado ou inválido não pode gerar novos tokens.
* Ao renovar a sessão, o refresh token anterior deve ser invalidado e substituído por um novo.
* A reutilização de um refresh token já utilizado deve ser detectada e tratada com segurança.
* O endpoint `/auth/logout` deve revogar o refresh token utilizado na sessão.
* Usuários desativados não podem renovar suas sessões.
* O logout deve impedir novas renovações com o refresh token revogado. Access tokens já emitidos continuam válidos até expirarem, a menos que seja implementado um mecanismo adicional de revogação.

### Autorização e RBAC

O sistema deve possuir três funções:

* `user`
* `moderator`
* `admin`

As permissões devem seguir estas regras:

| Operação | Permissão |
|---|---|
| Consultar o próprio perfil | Todos os usuários autenticados |
| Listar usuários | Moderator ou admin |
| Consultar outro usuário | Próprio usuário ou admin |
| Alterar a função de um usuário | Somente admin |
| Desativar ou reativar usuários | Somente admin |
| Alterar a própria senha | Todos os usuários autenticados |

* As permissões devem ser verificadas no backend.
* Não deve ser possível alterar a própria função para obter privilégios administrativos.
* A alteração de função deve aceitar apenas valores permitidos.
* Endpoints protegidos devem verificar as permissões exigidas para cada operação.
* Utilize dependências reutilizáveis para verificar as funções dos usuários.

### Gerenciamento de usuários

* O email deve ser único.
* A senha deve ser armazenada com hash seguro.
* A alteração de senha deve exigir a senha atual.
* A alteração de senha deve invalidar as sessões de refresh existentes do usuário.
* Não deve ser possível consultar ou alterar um usuário inexistente.
* Os dados recebidos devem ser validados com Pydantic.

## Organização

* Utilize routers separados para `/auth` e `/usuarios`.
* Mantenha modelos SQLAlchemy, schemas Pydantic, configuração do banco e lógica de segurança separados.
* Utilize `Depends` para recuperar o usuário autenticado e verificar suas permissões.
* Mantenha a lógica de criação, validação, renovação e revogação dos refresh tokens organizada e separada das rotas.

## O que este exercício acrescenta

Nos exercícios anteriores, você implementou autenticação com JWT e autorização baseada na propriedade dos recursos.

Agora, deverá evoluir esse conhecimento implementando renovação e gerenciamento de sessões, além de controlar as permissões de cada usuário por meio de RBAC.

O principal desafio será integrar autenticação, sessões e autorização sem permitir que tokens revogados sejam reutilizados ou que usuários obtenham permissões indevidas.

**Não implemente recuperação de senha por email, autenticação em dois fatores ou rate limiting neste exercício.** Esses recursos poderão ser trabalhados posteriormente.

> **Observação:** o fluxo OAuth2 Password é utilizado aqui para fins didáticos. Ele não é recomendado para novos sistemas de autenticação de usuários. O objetivo é compreender sua integração com o FastAPI e aprofundar os conceitos de JWT, refresh tokens e controle de acesso.