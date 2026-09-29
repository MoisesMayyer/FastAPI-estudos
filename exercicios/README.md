# Exercícios FastAPI

Exercícios práticos organizados em **níveis progressivos**, do básico ao avançado.  
Cada nível introduz novos conceitos e aumenta a complexidade gradualmente.

---

## Visão Geral dos Níveis

| Nível | Foco Principal | Conceitos-Chave | Status |
|-------|----------------|-----------------|--------|
| [nivel-1](nivel-1/README.md) | Fundamentos | Rotas, Path/Query Parameters, lógica Python | ✅ Completo (10 exercícios) |
| [nivel-2](nivel-2/) | Banco de Dados | SQLAlchemy, Models, CRUD, Relacionamentos, Routers | 🚧 Em andamento (2/10 exercícios) |
| [nivel-3](nivel-3/README.md) | *A definir* | — | 🔒 Não planejado |
| [nivel-4](nivel-4/README.md) | *A definir* | — | 🔒 Não planejado |
| [nivel-5](nivel-5/README.md) | *A definir* | — | 🔒 Não planejado |

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

## Progressão Recomendada

1. **Domine o nível 1** antes de avançar — entenda parâmetros, tipos e retorno JSON
2. **No nível 2**, foque no fluxo: `Router → Model → Database → Response` — ainda há muitos exercícios por vir
3. **Níveis 3+** serão definidos conforme a evolução do nível 2

> Cada exercício foi criado baseado na minha dificuldade real no momento, com apoio de IA para estruturação e boas práticas.

---

## Estrutura de Pastas

```
exercicios/
├── nivel-1/           # 10 exercícios - 1 arquivo cada
│   ├── ex001.py ... ex010.py
│   └── README.md      # Detalhamento de cada exercício
├── nivel-2/           # 10 exercícios planejados (2 feitos) - estrutura modular
│   ├── ex001/         # Produtos (CRUD simples)
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── database.py
│   │   ├── routers.py
│   │   └── README.md
│   ├── ex002/         # Biblioteca (Relacionamentos)
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── database.py
│   │   ├── autores_rotas.py
│   │   ├── livros_rotas.py
│   │   └── README.md
│   ├── ex003/         # (próximo)
│   ├── ex004/         # (próximo)
│   │   ...
│   └── sqlalchemy-exercicios/  # Exemplos extras
├── nivel-3/           # (vazio - não planejado)
├── nivel-4/           # (vazio - não planejado)
└── nivel-5/           # (vazio - não planejado)
```

---

## Dicas de Estudo

- **Leia o README** do nível/exercício antes de codar
- **Tente resolver sozinho** primeiro, depois compare
- **Use `/docs`** para testar cada endpoint
- **Quebre o código** de propósito para ver os erros
- **Commit frequente** — acompanhe sua evolução