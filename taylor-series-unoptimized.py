from math import factorial

def taylor_series_exp_unoptimized(x, n):
    """
    Calcula e^x usando a série de Taylor com n termos.
    Faz o cálculo direto de k! usando math.factorial.
    """
    result = 0.0  # Soma inicial
    for k in range(n):
        term = (x ** k) / factorial(k)  # Calcula diretamente x^k / k!
        result += term  # Soma o termo ao resultado
    return result

def calculate_exp_unoptimized(x, n):
    """
    Calcula e^x para x >= 0 diretamente e para x < 0 usando 1/e^(-x).
    """
    if x >= 0:
        return taylor_series_exp_unoptimized(x, n), None
    else:
        direct_result = taylor_series_exp_unoptimized(x, n)
        inverse_result = 1 / taylor_series_exp_unoptimized(-x, n)  # Usando y = -x
        return direct_result, inverse_result

# Exemplo de uso
x = float(input("Digite o valor de x: "))
n = int(input("Digite o número de termos (n): "))

# Cálculo de e^x
direct, inverse = calculate_exp_unoptimized(x, n)

# Exibição dos resultados
print(f"Resultado de e^{x} calculado diretamente pela série de Taylor: {direct}")
if inverse is not None:
    print(f"Resultado de e^{x} calculado como 1/e^(-x): {inverse}")
