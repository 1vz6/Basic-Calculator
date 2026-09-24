# Calculadora em Python

Projeto de uma calculadora de terminal desenvolvida em Python para praticar funções, dicionários, loops, tratamento de erros e armazenamento de dados.

## Funcionalidades atuais

- Realiza operações de:
  - Soma (`+`)
  - Subtração (`-`)
  - Multiplicação (`*`)
  - Divisão (`/`)
- Usa funções separadas para cada operação.
- Usa um dicionário para relacionar cada símbolo à sua respectiva função.
- Aceita números decimais usando `float`.
- Verifica se o operador informado é válido.
- Impede divisão por zero.
- Trata entradas numéricas inválidas com `try/except`.
- Guarda as operações realizadas em um histórico.
- Permite utilizar o resultado anterior como primeiro número da próxima operação.
- Exibe o histórico antes de encerrar a calculadora.

## Tecnologias

- Python 3
- Módulo `logo`, usado para exibir a logo da calculadora.

## Como funciona

As operações são armazenadas em um dicionário:

```python
values = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
```

Assim, o programa pode selecionar a função correspondente ao símbolo informado pelo usuário.

O resultado da última operação também é armazenado em:

```python
previous_result
```

Isso permite continuar uma sequência de cálculos usando o resultado anterior.

### Exemplo

```text
10 + 5 = 15
15 * 2 = 30
30 - 10 = 20
```

## Histórico

As operações ficam armazenadas no dicionário `historys`, usando a operação como chave e o resultado como valor.

Exemplo:

```python
{
    "10.0 + 5.0 =": 15.0,
    "15.0 * 2.0 =": 30.0
}
```

## Tratamento de erros

O projeto possui tratamento para valores numéricos inválidos:

```python
except ValueError:
    print("Um valor numérico inválido foi digitado")
```

Também verifica operadores inválidos e divisão por zero.

## Estrutura do projeto

```text
.
├── calc.py
└── logo.py
```

O arquivo `calc.py` contém a lógica principal da calculadora e importa a logo a partir de `logo.py`.

## Como executar

No terminal, dentro da pasta do projeto:

```bash
python calc.py
```

## Objetivo do projeto

Este projeto faz parte do aprendizado de Python e serve para praticar conceitos como:

- funções
- `return`
- dicionários
- chaves e valores
- loops `while` e `for`
- condicionais
- `try/except`
- `float`
- entrada de dados com `input()`
- armazenamento de resultados
- reutilização de valores anteriores
