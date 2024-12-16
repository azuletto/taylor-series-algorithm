# Taylor Series Computation in Python

Este repositório contém uma implementação em Python para calcular \( e^x \) utilizando a **série de Taylor**. O projeto faz parte da avaliação final da disciplina de **Cálculo Simbólico** no curso de Bacharelado em Ciência da Computação.

[![View PDF](https://img.shields.io/badge/View-PDF-blue)](link_para_o_pdf_aqui)

---

## Objetivo do Projeto

O programa realiza o cálculo de \( e^x \) com base na expansão da série de Taylor. Os principais aspectos abordados incluem:

1. **Cálculo para \( e^x \):**
   - Para valores positivos e negativos de \( x \).
   - Alternativa para valores negativos: \( e^x = 1 / e^{-x} \).

2. **Prevenção de overflow:**
   - Otimização do cálculo de \( k! \) para evitar valores excessivamente grandes.

3. **Critério de parada:**
   - Implementação de uma condição para interromper o cálculo com base na contribuição marginal dos termos adicionais.

4. **Suporte a computação simbólica:**
   - Integração de bibliotecas como `sympy` para validação dos resultados numéricos.

---

## Como Executar

### Requisitos

- Python 3.8 ou superior
- Instale as dependências com o comando:
  ```bash
  pip install -r requirements.txt
