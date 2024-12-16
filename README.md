# Taylor Series Computation in Python  

[![Project PDF](https://img.shields.io/badge/Document-PDF-blue)](link_para_seu_documento.pdf)  

This repository contains the implementation of a Python program for calculating \( e^x \) using the **Taylor series expansion**. This project is part of a competitive evaluation for the **Symbolic Computation** course, designed to explore both numerical and analytical methods for solving mathematical problems programmatically.  

---

## **Project Overview**  

### **Objective**  
To implement, analyze, and optimize the computation of \( e^x \) using the Taylor series with \( n \) terms. The project addresses both theoretical and practical aspects of numerical computation, including handling negative inputs, avoiding computational overflows, and exploring symbolic computation for comparison purposes.  

---

## **Functionality**  

### **1. Taylor Series Implementation**  
The Taylor series expansion for \( e^x \) is given by:  
\[
e^x = \sum_{k=0}^{n} \frac{x^k}{k!}
\]  

The program supports:  
- **Input Parameters**:  
  - Value of \( x \): Can be any real number (positive or negative).  
  - Number of terms \( n \): Determines the precision of the approximation.  

- **Handling Negative Inputs**:  
  - Direct computation using \( x \) in the Taylor series.  
  - Alternative computation using \( y = -x \), followed by \( e^x = 1 / e^{-x} \).  

---

### **2. Overflow Management**  
The calculation of factorial \( k! \) is optimized to prevent overflow by combining intermediate steps of the numerator \( x^k \) and the denominator \( k! \). This avoids excessively large intermediate values during computation.  

---

### **3. Precision and Stopping Criteria**  
A stopping criterion is implemented to interrupt the computation when the terms of the series become negligibly small, improving both performance and precision.  

---

### **4. Symbolic Computation Integration**  
The program integrates symbolic computation to:  
- Evaluate \( e^x \) symbolically using libraries like `sympy`.  
- Compare symbolic results with numerical approximations for accuracy and performance differences.  

---

## **Analysis and Testing**  

### **1. Test Cases**  
The program is tested with a wide range of inputs for \( x \) and \( n \):  
- **Values of \( x \)**:  
  - Near zero, to observe convergence and approximation accuracy.  
  - Far from zero, to test performance and stability.  

- **Values of \( n \)**:  
  - Small \( n \), to observe accuracy limitations.  
  - Large \( n \), to analyze computational performance and stopping criteria.  

---

### **2. Error Analysis**  
The following types of errors are identified and analyzed:  
- **Truncation Errors**: Resulting from using a finite number of terms in the Taylor series.  
- **Rounding Errors**: Arising from floating-point arithmetic during computations.  

---

### **3. Numerical vs Analytical Methods**  
The project differentiates between:  
- **Numerical Methods**: Approximations using finite terms of the Taylor series.  
- **Analytical Methods**: Symbolic computation of \( e^x \) to derive precise values.  

---

## **Execution Instructions**  

1. Clone the repository:  
   ```bash
   git clone https://github.com/username/taylor-series.git
   cd taylor-series
