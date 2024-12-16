def taylor_series_exp_fixed_terms(x, n):
    """
    Calcula e^x usando a série de Taylor com exatamente n termos fornecidos pelo usuário.
    """
    result = 1.0  # O primeiro termo da série (x^0 / 0!)
    term = 1.0    # Inicializa o termo como 1 (x^0 / 0!)
    
    for k in range(1, n):  # Itera exatamente n vezes
        term *= x / k  # Atualiza o termo incrementalmente
        result += term  # Soma o termo ao resultado
    
    return result

def calculate_exp_fixed_terms(x, n):
    """
    Calcula e^x de duas formas se x < 0:
    1. Direto pela série de Taylor.
    2. Usando y = -x e a fórmula 1/e^(-x).
    """
    direct_result = taylor_series_exp_fixed_terms(x, n)
    if x < 0:
        inverse_result = 1 / taylor_series_exp_fixed_terms(-x, n)
        return direct_result, inverse_result
    return direct_result, None

# Exemplo de uso
x = float(input("Digite o valor de x: "))
n = int(input("Digite o número de termos (n): "))

# Cálculo de e^x
direct, inverse = calculate_exp_fixed_terms(x, n)

# Exibição dos resultados
print(f"Valor de e^{x} calculado diretamente pela série de Taylor com {n} termos: {direct}")
if inverse is not None:
    print(f"Valor de e^{x} calculado como 1/e^(-x) com {n} termos: {inverse}")
