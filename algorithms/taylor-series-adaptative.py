def taylor_series_exp_adaptive(x, epsilon):
    """
    Calcula e^x usando a série de Taylor com um critério de parada adaptativo.
    O cálculo para quando o termo incremental é menor que a tolerância epsilon.
    """
    result = 1.0  # O primeiro termo da série (x^0 / 0!)
    term = 1.0    # Inicializa o termo como 1 (x^0 / 0!)
    k = 1         # Índice do termo
    
    while abs(term) > epsilon:  # Critério de parada baseado na tolerância
        term *= x / k  # Atualiza o termo incrementalmente
        result += term  # Soma o termo ao resultado
        k += 1  # Incrementa o índice do termo
    
    return result, k  # Retorna o valor calculado e o número de termos utilizados

def calculate_exp_adaptive(x, epsilon):
    """
    Calcula e^x de duas formas se x < 0 usando o critério adaptativo:
    1. Direto pela série de Taylor.
    2. Usando y = -x e a fórmula 1/e^(-x).
    """
    direct_result, terms_used = taylor_series_exp_adaptive(x, epsilon)
    if x < 0:
        inverse_result, inverse_terms_used = taylor_series_exp_adaptive(-x, epsilon)
        return direct_result, terms_used, 1 / inverse_result, inverse_terms_used
    return direct_result, terms_used, None, None

# Exemplo de uso
x = float(input("Digite o valor de x: "))
option = input("Escolha o método (1: número fixo de termos, 2: critério adaptativo): ")

if option == "1":
    n = int(input("Digite o número de termos (n): "))
    direct, inverse = calculate_exp_fixed_terms(x, n)
    print(f"Valor de e^{x} calculado diretamente pela série de Taylor com {n} termos: {direct}")
    if inverse is not None:
        print(f"Valor de e^{x} calculado como 1/e^(-x) com {n} termos: {inverse}")
elif option == "2":
    epsilon = float(input("Digite o valor da tolerância (epsilon): "))
    direct, terms, inverse, inverse_terms = calculate_exp_adaptive(x, epsilon)
    print(f"Valor de e^{x} calculado diretamente pela série de Taylor com tolerância {epsilon}: {direct}")
    print(f"Número de termos utilizados: {terms}")
    if inverse is not None:
        print(f"Valor de e^{x} calculado como 1/e^(-x) com tolerância {epsilon}: {inverse}")
        print(f"Número de termos utilizados no cálculo inverso: {inverse_terms}")
else:
    print("Opção inválida!")
