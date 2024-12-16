# Exponential Calculation Using Taylor Series

[![PDF Document](https://img.shields.io/badge/PDF-Document-blue?style=flat&logo=adobe)](link_para_o_pdf)  

## **Project Overview**

This project implements a Python program to compute the exponential function $\( e^x \) using its **Taylor Series Expansion**. The program also incorporates optimizations to handle negative values of \( x \), prevent factorial overflow, and determine a stopping criterion for series convergence.

---

## **Objectives**

1. **Implement Taylor Series**: Calculate \( e^x \) using the Taylor series formula up to \( n \) terms, where \( x \) and \( n \) are user inputs.
2. **Handling Negative Values**: Evaluate \( e^x \) in two ways for \( x < 0 \):
   - Directly using the series.
   - Using the transformation \( y = -x \) and computing \( e^x = \frac{1}{e^{-x}} \).
3. **Avoiding Overflow**: Optimize factorial calculations to prevent overflow by performing intermediate divisions.
4. **Convergence Criterion**: Determine the appropriate stopping condition for the Taylor series expansion.
5. **Numerical vs Analytical Methods**: Analyze the differences and types of errors in the results.
6. **Symbolic Computation**: Explore symbolic computation to verify results and analyze performance.

---

## **Requirements**

- **Python 3.x**
- Libraries:
  - `math` (for numerical operations)
  - `sympy` (for symbolic computation)

---

## **Usage**

### **1. Execution Instructions**

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/taylor-series-exp.git
   cd taylor-series-exp
