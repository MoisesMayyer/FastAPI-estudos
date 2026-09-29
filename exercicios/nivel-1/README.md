# Nível 1 — Fundamentos do FastAPI

Objetivo: aprender os fundamentos do FastAPI através de exercícios pequenos e progressivos, focando em **rotas, parâmetros e lógica Python**.

> Neste nível, cada exercício deve ficar em um único arquivo `.py`.
> Não utilizar ainda Pydantic, APIRouter, banco de dados ou outras estruturas.

## Progressão

| Exercício | Dificuldade | Tema principal                   |
| --------- | ----------- | -------------------------------- |
| EX001     | 🟢 Fácil    | Primeira rota e Path Parameter   |
| EX002     | 🟢 Fácil    | Múltiplos parâmetros e operações |
| EX003     | 🟢 Fácil    | Condicionais e tipos             |
| EX004     | 🟡 Médio    | Lógica + múltiplos parâmetros    |
| EX005     | 🟡 Médio    | Query Parameters                 |
| EX006     | 🟡 Médio    | Regras de negócio                |
| EX007     | 🟡 Médio    | Query Parameters + loops         |
| EX008     | 🔴 Difícil  | Processamento de listas          |
| EX009     | 🔴 Difícil  | Lógica mais elaborada            |
| EX010     | 🔴 Difícil  | Combinação de vários conceitos   |

---

## 🟢 Fácil

### EX001 — Saudação personalizada

Crie uma rota:

```text
GET /ola/{nome}
```

Receba o nome pela URL e retorne uma mensagem personalizada.

Exemplo:

```text
/ola/Moises
```

Resposta esperada:

```json
{
  "message": "Olá, Moises!"
}
```

**Conceitos:** FastAPI, criação de rotas e Path Parameters.

---

### EX002 — Calculadora

Crie uma rota que receba dois números e retorne:

* Soma
* Subtração
* Multiplicação
* Divisão

Exemplo:

```text
/calcular/10/2
```

**Conceitos:** múltiplos parâmetros, tipos e operações matemáticas.

---

### EX003 — Analisador de número

Receba um número e informe:

* Se é positivo, negativo ou zero
* Se é par ou ímpar
* Seu dobro
* Seu quadrado

**Conceitos:** parâmetros, condicionais e lógica Python.

---

## 🟡 Médio

### EX004 — Média do aluno

Receba o nome de um aluno e três notas.

Retorne:

* Nome
* Notas
* Média
* Situação

Crie uma regra para determinar se o aluno foi aprovado ou reprovado.

**Conceitos:** múltiplos parâmetros, operações e condicionais.

---

### EX005 — Conversor de temperatura

Crie uma API capaz de converter entre:

* Celsius
* Fahrenheit
* Kelvin

Exemplo:

```text
/converter?valor=30&de=celsius&para=fahrenheit
```

**Conceitos:** Query Parameters, condicionais e funções matemáticas.

---

### EX006 — Calculadora de desconto

Receba:

* Preço
* Percentual de desconto

Retorne:

* Preço original
* Valor do desconto
* Preço final

**Conceitos:** Query/Path Parameters e regras de negócio.

---

### EX007 — Tabuada

Receba um número e um limite.

Exemplo:

```text
/tabuada/7?limite=10
```

Retorne a tabuada do número informado até o limite.

**Conceitos:** Query Parameters, `for` e listas.

---

## 🔴 Difícil

### EX008 — Analisador de números

Receba vários números e retorne:

* Quantidade de números
* Maior número
* Menor número
* Soma
* Média
* Quantidade de pares
* Quantidade de ímpares

**Conceitos:** listas, loops, condicionais e processamento de dados.

---

### EX009 — Boletim escolar

Receba o nome de um aluno e várias notas.

Calcule:

* Média
* Maior nota
* Menor nota
* Quantidade de notas acima da média
* Situação final

Crie regras para:

* Aprovação
* Recuperação
* Reprovação

**Conceitos:** listas, loops, condicionais e organização da lógica.

---

### EX010 — Sistema de compra

Crie uma API que receba:

* Produto
* Preço
* Quantidade
* Forma de pagamento

Calcule o valor total e aplique regras diferentes:

| Forma de pagamento | Regra        |
| ------------------ | ------------ |
| Dinheiro           | Desconto     |
| Pix                | Desconto     |
| Cartão             | Preço normal |
| Parcelado          | Acréscimo    |

Retorne um resumo completo da compra.

Exemplo de informações:

```json
{
  "produto": "Teclado",
  "quantidade": 2,
  "subtotal": 200,
  "desconto": 20,
  "acrescimo": 0,
  "total": 180
}
```

**Conceitos:** parâmetros, condicionais, cálculos e combinação dos conceitos anteriores.

---

## Objetivo ao terminar o nível

Ao finalizar os 10 exercícios, você deve conseguir criar uma aplicação FastAPI simples sabendo:

* Criar uma aplicação com `FastAPI()`
* Criar endpoints
* Utilizar métodos HTTP
* Trabalhar com Path Parameters
* Trabalhar com Query Parameters
* Definir tipos dos parâmetros
* Retornar dados em JSON
* Utilizar lógica Python dentro dos endpoints

**Próximo nível:** aprofundar parâmetros, validação e começar a introduzir Pydantic.
