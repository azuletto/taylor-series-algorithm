# Taylor Series Computation in Python

[![View PDF](https://img.shields.io/badge/View-PDF-blue)](link_to_your_pdf_here)  

This repository contains a Python implementation to compute \( e^x \) using the **Taylor series expansion**. The project was developed as part of an evaluation for the **Symbolic Computation** course in the Computer Science program.  

---

## Project Description

This project explores the numerical and analytical computation of \( e^x \) through its Taylor series representation. Key features include:  

1. **Calculation of \( e^x \) for positive and negative values of \( x \):**  
   - Direct computation using \( x \) in the series.  
   - Alternate computation using \( y = -x \), followed by \( e^x = 1 / e^{-x} \).  

2. **Optimization for factorial calculation:**  
   - Avoiding overflow by combining terms incrementally during the computation of \( \frac{x^k}{k!} \).  

3. **Precision control with stopping criteria:**  
   - The series stops calculating when terms become smaller than a defined threshold.  

4. **Symbolic computation support:**  
   - The integration of symbolic libraries (e.g., `sympy`) allows comparison of numerical and symbolic results.  

---

## How to Run

1. **Clone the Repository:**  
   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
