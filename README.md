# FastAPI Estudos

Projeto de aprendizado de **FastAPI** saindo do básico e evoluindo aos poucos, com prática contínua.

## Estrutura

O projeto está organizado em **níveis progressivos**:

- **nivel-1** - Fundamentos básicos (rotas, parâmetros, validação)
- **nivel-2** - Integração com banco de dados (SQLAlchemy, SQLite, modelos, migrações)
- **nivel-3** - *(em andamento)*
- **nivel-4** - *(em andamento)*
- **nivel-5** - *(em andamento)*

Também há a pasta `projetos/` com aplicações mais completas integrando os conceitos.

## Características

- **Do zero**: Tudo construído passo a passo, sem templates prontos
- **Banco de dados**: Uso de SQLite + SQLAlchemy desde os primeiros níveis
- **Exercícios personalizados**: Cada exercício reflete minha dificuldade real no momento
- **Apoio de IA**: Exercícios escritos e desenvolvidos com auxílio de inteligência artificial

## Como executar

```bash
# Criar ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows

# Instalar dependências
pip install fastapi uvicorn sqlalchemy

# Rodar um exercício
uvicorn exercicios.nivel-1.ex001:app --reload
```

## Objetivo

Consolidar conhecimento em FastAPI através de prática direcionada, evoluindo de conceitos simples para aplicações completas com persistência, autenticação e deploy.