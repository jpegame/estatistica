import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

def plot_p_value_area(z_value, test_type, title_suffix=""):
    """Esboça uma distribuição normal padrão e sombreia a área para o valor p."""
    x = np.linspace(-4, 4, 500)
    y = scipy.stats.norm.pdf(x)

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, color='blue')
    plt.axvline(0, color='gray', linestyle='--', linewidth=0.8, label='Média (0)')

    if test_type == "unilateral à esquerda":
        x_fill = np.linspace(-4, z_value, 100)
        y_fill = scipy.stats.norm.pdf(x_fill)
        plt.fill_between(x_fill, 0, y_fill, color='skyblue', alpha=0.6, label='Área p-valor')
        plt.axvline(z_value, color='red', linestyle='--', label=f'z = {z_value:.2f}')
        plt.title(f'Teste Unilateral à Esquerda {title_suffix}')
    elif test_type == "unilateral à direita":
        x_fill = np.linspace(z_value, 4, 100)
        y_fill = scipy.stats.norm.pdf(x_fill)
        plt.fill_between(x_fill, 0, y_fill, color='salmon', alpha=0.6, label='Área p-valor')
        plt.axvline(z_value, color='red', linestyle='--', label=f'z = {z_value:.2f}')
        plt.title(f'Teste Unilateral à Direita {title_suffix}')
    elif test_type == "bilateral":
        z_abs = abs(z_value)
        x_fill_left = np.linspace(-4, -z_abs, 100)
        y_fill_left = scipy.stats.norm.pdf(x_fill_left)
        plt.fill_between(x_fill_left, 0, y_fill_left, color='lightgreen', alpha=0.6, label='Área p-valor')

        x_fill_right = np.linspace(z_abs, 4, 100)
        y_fill_right = scipy.stats.norm.pdf(x_fill_right)
        plt.fill_between(x_fill_right, 0, y_fill_right, color='lightgreen', alpha=0.6)

        plt.axvline(-z_abs, color='red', linestyle='--', label=f'z = -{z_abs:.2f}')
        plt.axvline(z_abs, color='red', linestyle='--', label=f'z = {z_abs:.2f}')
        plt.title(f'Teste Bilateral {title_suffix}')
    else:
        plt.title('Distribuição Normal Padrão') # Fallback
        
    plt.xlabel('Z-score')
    plt.ylabel('Densidade de Probabilidade')
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.show()

# --- Afirmação 1 ---
print("\n1. Um analista de consumo informa que a vida média de certo tipo de bateria automotiva não é de 74 meses.")
# a. Expresse H0 e Ha em palavras e em símbolos.
H0_simbolo_1 = "μ = 74"
Ha_simbolo_1 = "μ ≠ 74"
print(f"a. H₀ (palavras): A vida média da bateria é de 74 meses. (Símbolo: {H0_simbolo_1})")
print(f"   Hₐ (palavras): A vida média da bateria NÃO é de 74 meses. (Símbolo: {Ha_simbolo_1})")
# b. Determine se o teste é unilateral à esquerda, unilateral à direita ou bilateral.
tipo_teste_1 = "bilateral"
print(f"b. O teste é: {tipo_teste_1} (pois Hₐ contém ≠)")
# c. Esboce a distribuição normal padrão e sombreie a área para o valor p.
plot_p_value_area(1.5, tipo_teste_1, " (μ ≠ 74)")

# --- Afirmação 2 ---
print("\n2. Um corretor de imóveis divulga que a proporção de proprietários que acham suas casas muito pequenas para suas famílias é mais que 24%.")
# a. Expresse H0 e Ha em palavras e em símbolos.
H0_simbolo_2 = "p ≤ 0.24"
Ha_simbolo_2 = "p > 0.24"
print(f"a. H₀ (palavras): A proporção de proprietários é menor ou igual a 24%. (Símbolo: {H0_simbolo_2})")
print(f"   Hₐ (palavras): A proporção de proprietários é mais que 24%. (Símbolo: {Ha_simbolo_2})")
# b. Determine se o teste é unilateral à esquerda, unilateral à direita ou bilateral.
tipo_teste_2 = "unilateral à direita"
print(f"b. O teste é: {tipo_teste_2} (pois Hₐ contém >)")
# c. Esboce a distribuição normal padrão e sombreie a área para o valor p.
# Para sombrear, usamos um exemplo de z-estatística, por exemplo, 1.0, para o plot
plot_p_value_area(1.0, tipo_teste_2, " (p > 0.24)")