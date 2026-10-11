# FastAPI Estudos

Repositório dedicado ao meu aprendizado prático de FastAPI, com exercícios progressivos para desenvolver minhas habilidades em construção de APIs REST, integração com banco de dados e autenticação.

O projeto é dividido em níveis, cada um introduzindo novos conceitos e aprofundando os conhecimentos adquiridos anteriormente.

## Estrutura do projeto

- **Nível 1 — Fundamentos**: rotas, parâmetros, métodos HTTP e validações básicas.
- **Nível 2 — Pydantic e banco de dados**: validação e estruturação de dados com Pydantic, persistência com SQLite, SQLAlchemy e migrações.
- **Nível 3 — Autenticação e segurança**: OAuth2, JWT e autenticação de usuários. (Em desenvolvimento)
- **Nível 4 — Em planejamento**
- **Nível 5 — Em planejamento**

A pasta `projetos/` contém aplicações mais completas, desenvolvidas para aplicar os conceitos estudados na prática.

## Tecnologias e ferramentas

- Python
- FastAPI
- Pydantic
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
