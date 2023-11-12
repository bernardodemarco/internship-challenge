# Desafio SC Clouds

Esse documento consiste na resolução do desafio proposto pela empresa SC Clouds para vaga de desenvolvedor.

## Sumário

1. [Questões Conceituais](#questões-conceituais)

   1. [Questão 1](#questão-1)
   2. [Questão 2](#questão-2)
   3. [Questão 3](#questão-3)

2. [Questões Práticas](#questões-práticas)

## Questões Conceituais

Segue as respostas relacionadas às perguntas conceituais propostas no desafio.

### Questão 1

### Questão 2

### Questão 3

## Questões Práticas

### Estrutura de pastas

```bash
  ├── .gitignore
  ├── README.md # respostas em arquivo MD
  ├── answers.pdf # respostas em arquivo PDF
  ├── main.py # arquivo do programa a ser executado
  ├── fibonacci
  │   ├── main.py # arquivo principal FIBONACCI
  │   ├── fib.py # algoritmo linear
  │   └── recursive_fib.py # algoritmo recursivo
  ├── prime_numbers
  │   ├── main.py # arquivo principal PRIME NUMBERS
  │   ├── is_prime.py # algoritmo linear
  │   └── recursive_is_prime.py # algoritmo recursivo
  │
```

### Setup

Para rodar os algoritmos localmente, certifique-se que a versão do Python seja igual ou superior à 3.10.12 e siga as próximas instruções:

```bash
    # clone o projeto
    git clone https://github.com/bernardodemarco/sc-clouds-challenge.git

    # rodar o projeto
    cd sc-clouds-challenge
    python3 main.py
```

Ressalta-se que para rodar os algoritmos foi criado um menu intuitivo para navegar entre as resoluções.

### Sobre a documentação dos algoritmos

Foi criada uma breve documentação dos algoritmos usando [docstrings](https://peps.python.org/pep-0257/), seguindo o seguinte padrão:

```python
    def docs_pattern():
        """
        Brief description.

        Args:
            <parameter_name> (<parameter_type>): <parameter description>.

        Returns:
            <return_type>: <return_description>.
        """
        pass
```

Além disso, ressalta-se que foram adicionadas tipagens do Python, visando melhorar a legibilidade do código.
