# Exercícios FastAPI

Exercícios práticos organizados em **níveis progressivos**, do básico ao avançado.  
Cada nível introduz novos conceitos e aumenta a complexidade gradualmente.

---

## Visão Geral dos Níveis

| Nível | Foco Principal | Conceitos-Chave | Status |
|-------|----------------|-----------------|--------|
| [nivel-1](nivel-1/) | Fundamentos | Rotas, Path/Query Parameters, lógica Python | ✅ Completo (10 exercícios) |
| [nivel-2](nivel-2/) | Banco de Dados | SQLAlchemy, **Pydantic**, Models, CRUD, Relacionamentos, Routers | ✅ Completo  (4/4 exercícios) ||
| [nivel-3](nivel-3/) | Autenticação & Segurança | Hash de senhas (Argon2), JWT, OAuth2 Password Flow, OAuth2PasswordBearer, OAuth2PasswordRequestForm, Refresh Tokens, Proteção de rotas | ✅ Planejado (3 exercícios: ex-001, ex-002, ex-003) |
| [nivel-4](nivel-4/) | *A definir* | — | 🔒 Não planejado |
| [nivel-5](nivel-5/) | *A definir* | — | 🔒 Não planejado |

---

## Como Executar

```bash
# Na raiz do projeto
source .venv/bin/activate

# Nível 1 - arquivo único
uvicorn exercicios.nivel-1.ex001:app --reload

# Nível 2 - estrutura modular
uvicorn exercicios.nivel-2.ex001.main:app --reload
uvicorn exercicios.nivel-2.ex002.main:app --reload
```

Acesse a documentação automática em: **http://localhost:8000/docs**

---

---

## Níveis de Estudo

Os exercícios estão organizados por níveis de dificuldade e acompanham minha evolução no aprendizado de FastAPI.

- **Nível 1 — Fundamentos:** criação de endpoints, parâmetros, métodos HTTP, respostas JSON e operações básicas com FastAPI.
- **Nível 2 — Banco de Dados:** desenvolvimento de APIs com SQLAlchemy, persistência de dados, relacionamentos entre tabelas, Pydantic e organização do código em módulos.
- **Nível 3 — Autenticação e Segurança:** cadastro de usuários, hash de senhas, autenticação com JWT, OAuth2 e proteção de rotas.
- **Nível 4 — A definir:** novos exercícios serão planejados conforme meu avanço nos estudos.
- **Nível 5 — A definir:** reservado para conceitos mais avançados que serão definidos futuramente.

Cada nível introduz novos conceitos e aumenta gradualmente a complexidade dos projetos.

## Estrutura de Pastas

A pasta `exercicios/` contém os projetos desenvolvidos durante os estudos, separados por nível.

```text
exercicios/
├── nivel-1/
│   ├── ex001.py ... ex010.py
│   └── README.md
│
├── nivel-2/
│   ├── ex001/
│   ├── ex002/
│   ├── ex003/
│   ├── ex004/
│   ├── ...
│   ├── sqlalchemy-exercicios/
│   └── README.md
│
├── nivel-3/
│   ├── ex-001/
│   ├── ex-002/
│   ├── ex-003/
│   └── README.md
│
├── nivel-4/
└── nivel-5/
```

### O que você encontra em cada nível?

**`nivel-1/` — Exercícios introdutórios**

Exercícios menores, com arquivos Python individuais, para praticar os fundamentos do FastAPI e entender como criar e testar endpoints.

**`nivel-2/` — APIs com banco de dados**

Projetos com estrutura modular, separando responsabilidades entre arquivos. Aqui pratico CRUD, SQLAlchemy, modelos, sessões de banco de dados, relacionamentos e validação de dados.

Cada exercício possui seu próprio README com o enunciado e os requisitos.

**`nivel-3/` — Autenticação e segurança**

Projetos voltados à autenticação de usuários, armazenamento seguro de senhas, JWT, OAuth2 e proteção de endpoints. O objetivo é aprender a controlar quem pode acessar cada recurso da API.

**`nivel-4/` e `nivel-5/` — Próximas etapas**

Ainda não possuem exercícios definidos. Serão preenchidos conforme eu avançar e identificar os próximos conceitos que preciso estudar.

## Como Utilizar os Exercícios

1. Leia o README do exercício para entender o problema e os requisitos.
2. Implemente a solução por conta própria, consultando a documentação quando necessário.
3. Utilize o `/docs` do FastAPI para testar os endpoints.
4. Revise os erros encontrados e melhore a implementação conforme aprende novos conceitos.
5. Consulte o histórico de commits para acompanhar a evolução do código.

## Sobre o Projeto

Este repositório documenta minha evolução prática no aprendizado de Python e FastAPI. Os exercícios partem de problemas simples e evoluem gradualmente para APIs mais completas.

Os enunciados são baseados nas minhas dificuldades reais durante os estudos, com apoio de ferramentas de IA na organização dos exercícios e na pesquisa de boas práticas. A implementação e o aprendizado acontecem ao longo da resolução de cada desafio.

O objetivo é construir uma base sólida de desenvolvimento backend por meio da prática contínua.
