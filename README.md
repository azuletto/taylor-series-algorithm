# Exponential Calculation Using Taylor Series

[![PDF Document](https://img.shields.io/badge/PDF-Document-blue?style=flat&logo=adobe)](https://drive.google.com/file/d/1JjpXWa6qqrdpLRKv9WwijLpZjNHL9H_X/view?usp=sharing)  

## **Project Overview**

This project implements a Python program to compute the exponential function $e^x$ using its **Taylor Series Expansion**. The program also incorporates optimizations to handle negative values of $x$, prevent factorial overflow, and determine a stopping criterion for series convergence.

---

## **Objectives**

1. **Implement Taylor Series**: Calculate $e^x$ using the Taylor series formula up to $n$ terms, where $x$ and $n$ are user inputs.
2. **Handling Negative Values**: Evaluate $e^x$ in two ways for $x < 0$:
   - Directly using the series.
   - Using the transformation $y = -x$ and computing:
     $e^x = \frac{1}{e^{-x}}$
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

## **Theoretical Background**

### **1. Taylor Series Expansion**

The exponential function $e^x$ can be approximated by the **Taylor Series**:
$e^x = \sum_{k=0}^n \frac{x^k}{k!}$
(where $n$ is the number of terms).

For negative $x$, two approaches are considered:
1. Direct calculation using $x$ in the series.
2. Transforming $x$ to $y = -x$ and using:
   $e^x = \frac{1}{e^{-x}}$

### **2. Overflow Prevention**

The factorial $k!$ grows rapidly, leading to overflow. To mitigate this, the $k$-th term in the series $\frac{x^k}{k!}$ is computed iteratively:

$\text{term}_k = \frac{\text{term}_{k-1} \cdot x}{k}$

This avoids explicit computation of $k!$.

### **3. Stopping Criterion**

The series calculation terminates when the relative change between consecutive terms becomes negligibly small:
$\frac{\text{term}_k}{\text{sum}} < \text{threshold}$
where `threshold` is a small predefined value, e.g., $10^{-6}$.

---

## **Numerical vs Analytical Methods**

| **Aspect**          | **Analytical Method**                          | **Numerical Method**                          |
|----------------------|-----------------------------------------------|----------------------------------------------|
| **Definition**       | Exact solutions derived from formulas.       | Approximations using iterative calculations. |
| **Nature**           | Symbolic and exact.                          | Approximate and dependent on precision.      |
| **Example**          | $e^x = \lim_{n \to \infty} (1 + x/n)^n$      | Taylor series expansion for $e^x$.           |

---

## **License**

This project is licensed under the MIT License.  

You can read the full terms of the license in the [LICENSE](./LICENSE) file or visit:

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

