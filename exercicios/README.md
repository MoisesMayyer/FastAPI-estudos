# Exercícios FastAPI

Exercícios práticos de **FastAPI** organizados em níveis progressivos, do básico ao avançado. Cada nível apresenta novos conceitos e aumenta a complexidade aos poucos.

![Python](https://img.shields.io/badge/Python-3.14-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.142-009688?logo=fastapi&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-testes-0A9EDC?logo=pytest&logoColor=white)
![Níveis](https://img.shields.io/badge/n%C3%ADveis-1%20a%204-blue)

> **Projeto de estudo.** Cada exercício possui seu próprio enunciado em `README.md` e, quando concluído, a implementação da solução.

## Sumário

- [Visão geral](#visão-geral)
- [Como executar](#como-executar)
- [Estrutura de pastas](#estrutura-de-pastas)
- [O que você encontra em cada nível](#o-que-você-encontra-em-cada-nível)
- [Glossário rápido](#glossário-rápido)
- [Como utilizar os exercícios](#como-utilizar-os-exercícios)
- [Sobre o projeto](#sobre-o-projeto)

## Visão geral

| Nível | Tema | O que você pratica | Situação |
|-------|------|--------------------|----------|
| [nivel-1](nivel-1/) | Fundamentos | Rotas, parâmetros de caminho e de consulta, métodos HTTP, respostas JSON | ✅ Completo (10 exercícios) |
| [nivel-2](nivel-2/) | Banco de dados | SQLAlchemy, Pydantic, CRUD, relacionamentos, routers | ✅ Completo (4/4 exercícios) |
| [nivel-3](nivel-3/) | Autenticação e segurança | Hash de senhas (Argon2), JWT, OAuth2, refresh tokens, RBAC | 🟡 Em andamento (4/5 exercícios) |
| [nivel-4](nivel-4/) | Testes automatizados | Pytest, `TestClient`, fixtures, isolamento de banco | 🟡 Em andamento (4/5 exercícios) |
| [nivel-5](nivel-5/) | A definir | — | 🔒 Não planejado |

**Legenda:** ✅ Completo · 🟡 Em andamento · 🔒 Não planejado

## Como executar

**Pré-requisitos:** Python 3.14 ou superior e as dependências do projeto instaladas.

```bash
# 1. Na raiz do repositório, ative o ambiente virtual
source .venv/bin/activate

# 2. Execute o exercício a partir da pasta dele
cd exercicios/nivel-1
uvicorn ex001:app --reload

cd exercicios/nivel-2/ex012
uvicorn main:app --reload

# 3. Nos exercícios com testes (nível 4)
cd exercicios/nivel-4/ex021
pytest
```

Depois de iniciar a API, a documentação interativa fica disponível em **http://localhost:8000/docs**.

## Estrutura de pastas

A pasta `exercicios/` reúne os exercícios separados por nível. Cada exercício tem seu próprio diretório e o enunciado no `README.md`.

```text
exercicios/
├── README.md
├── nivel-1/
│   ├── ex001.py ... ex010.py
│   └── README.md
├── nivel-2/
│   ├── ex011/
│   ├── ex012/
│   ├── ex013/
│   ├── ex014/
│   └── ex015/
├── nivel-3/
│   ├── ex016/
│   ├── ex017/
│   ├── ex018/
│   ├── ex019/
│   └── ex020/
├── nivel-4/
│   ├── ex021/
│   ├── ex022/
│   ├── ex023/
│   └── ex024/
└── nivel-5/
```

## O que você encontra em cada nível

### Nível 1 — Fundamentos

O ponto de partida. São exercícios menores, em arquivos únicos, para entender como uma API recebe requisições e devolve respostas.

**Você pratica:**

- criação de endpoints;
- parâmetros de caminho e de consulta;
- métodos HTTP;
- respostas em JSON;
- validação e teste dos endpoints pelo `/docs`.

### Nível 2 — Banco de dados

Aqui os dados passam a ser salvos de verdade. O código é dividido em módulos, com responsabilidades separadas entre rotas, modelos, validação e acesso ao banco.

**Você pratica:**

- CRUD completo;
- models com SQLAlchemy;
- validação com Pydantic;
- relacionamentos entre tabelas;
- organização de routers;
- sessões e persistência no banco.

### Nível 3 — Autenticação e segurança

Projetos voltados ao controle de quem pode acessar cada recurso da API.

**Você pratica:**

- cadastro de usuários e hash de senhas;
- autenticação com JWT;
- fluxo OAuth2 Password;
- refresh tokens e renovação de sessão;
- RBAC (controle de acesso por função);
- proteção de rotas e permissões.

### Nível 4 — Testes automatizados

Exercícios voltados à verificação automática das APIs, sem depender de testes manuais no `/docs`.

**Você pratica:**

- testes com Pytest;
- requisições com `TestClient`;
- fixtures para reutilizar dados e configurações;
- testes de CRUD e de respostas HTTP;
- isolamento do banco de dados nos testes;
- testes de integração com FastAPI e SQLAlchemy.

### Nível 5 — Próximas etapas

Ainda não possui exercícios definidos. Será preenchido conforme eu avançar e identificar os próximos conceitos que preciso estudar.

## Glossário rápido

- **API:** conjunto de rotas que permite a comunicação entre sistemas.
- **Endpoint:** cada endereço da API, como `GET /tarefas`.
- **CRUD:** as quatro operações básicas sobre dados — criar, consultar, atualizar e excluir.
- **JWT:** token assinado usado para identificar e autenticar o usuário.
- **Fixture:** dado ou configuração preparada para ser reutilizada em vários testes.
- **Pytest:** ferramenta que executa os testes automatizados.

## Como utilizar os exercícios

1. Leia o `README.md` do exercício para entender o problema e os requisitos.
2. Implemente a solução por conta própria, consultando a documentação quando necessário.
3. Use o `/docs` do FastAPI para testar os endpoints.
4. Revise os erros encontrados e melhore a implementação conforme aprender novos conceitos.
5. Consulte o histórico de commits para acompanhar a evolução do código.

## Sobre o projeto

Este repositório documenta minha evolução prática no aprendizado de Python e FastAPI. Os exercícios partem de problemas simples e evoluem gradualmente para APIs mais completas.

Os enunciados são baseados nas minhas dificuldades reais durante os estudos, com apoio de ferramentas de IA na organização dos exercícios e na pesquisa de boas práticas. A implementação e o aprendizado acontecem ao longo da resolução de cada desafio.

O objetivo é construir uma base sólida de desenvolvimento backend por meio da prática contínua.
