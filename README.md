# FastAPI Estudos

Repositório de estudos práticos de **FastAPI**, organizado em níveis progressivos: dos fundamentos de rotas e parâmetros até autenticação, segurança e testes automatizados.

![Python](https://img.shields.io/badge/Python-3.14-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.142-009688?logo=fastapi&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.1-D71F00)
![Pydantic](https://img.shields.io/badge/Pydantic-2.13-E92063)
![Pytest](https://img.shields.io/badge/Pytest-testes-0A9EDC?logo=pytest&logoColor=white)
![Status](https://img.shields.io/badge/exerc%C3%ADcios-em%20andamento-yellow)

> **Projeto de estudo.** Este repositório documenta minha evolução prática em Python e FastAPI, com exercícios organizados em níveis progressivos e implementação própria.

## Sumário

- [Estrutura do projeto](#estrutura-do-projeto)
- [Tecnologias e ferramentas](#tecnologias-e-ferramentas)
- [Metodologia](#metodologia)
- [Como executar](#como-executar)
- [Objetivo](#objetivo)

## Estrutura do projeto

- **Nível 1 — Fundamentos**: rotas, parâmetros, métodos HTTP e validações básicas.
- **Nível 2 — Pydantic e banco de dados**: validação e estruturação de dados com Pydantic, persistência com SQLite, SQLAlchemy e migrações.
- **Nível 3 — Autenticação e segurança**: OAuth2, JWT e autenticação de usuários. (Em desenvolvimento)
- **Nível 4 — Testes automatizados**: Pytest, `TestClient`, fixtures, isolamento de banco e testes de integração com FastAPI e SQLAlchemy. (Em desenvolvimento)
- **Nível 5 — Em planejamento**

## Tecnologias e ferramentas

- Python
- FastAPI
- Pydantic
- Pytest
- SQLAlchemy
- SQLite
- Uvicorn

Novas tecnologias serão adicionadas conforme avançar nos estudos.

## Metodologia

- **Aprendizado progressivo**: cada nível parte dos conhecimentos anteriores.
- **Prática orientada**: exercícios desenvolvidos para trabalhar conceitos específicos e superar dificuldades.
- **Implementação própria**: código escrito e revisado durante o processo de aprendizagem, com apoio de documentação e ferramentas de IA.
- **Evolução contínua**: refatoração e aprimoramento dos exercícios à medida que novos conceitos são aprendidos.

## Como executar

Clone o repositório e acesse a pasta do projeto:

```bash
git clone https://github.com/MoisesMayyer/FastAPI-estudos
cd FastAPI-estudos
```

Crie e ative um ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate
```

No Windows, utilize:

```bash
.venv\Scripts\activate
```

Instale as dependências necessárias para o exercício escolhido e execute a aplicação. Por exemplo:

```bash
uvicorn exercicios.nivel_1.ex001:app --reload
```

O caminho do módulo deve corresponder à estrutura real dos arquivos do repositório.

## Objetivo

Consolidar meus conhecimentos em desenvolvimento backend com Python e FastAPI, evoluindo dos fundamentos de APIs REST para aplicações com persistência de dados, autenticação, segurança e deploy.

Este repositório documenta minha evolução prática como desenvolvedor backend.
