import scipy.stats
import matplotlib.pyplot as plt
import numpy as np

mu_0 = 13960
n = 500
x_barra = 13725
sigma = 2345

# Hipóteses: A afirmação é que o custo médio É de US$ 13.960.
# Isso implica um teste bilateral para ver se o custo médio é DIFERENTE.
# H0: μ = 13960
# Ha: μ ≠ 13960

niveis_significancia_alpha = [0.10, 0.01] # Níveis de significância a serem testados

# Calcule a estatística de teste padronizada z, que será a mesma para ambos os alphas
erro_padrao = sigma / np.sqrt(n)
z_estatistica = (x_barra - mu_0) / erro_padrao
print(f"Estatística de teste padronizada z = {z_estatistica:.2f}")

# Iterar sobre cada nível de significância para realizar o teste
for alpha in niveis_significancia_alpha:
    print(f"\n--- Para α = {alpha:.2f} ---")
    print(f"a. Nível de Significância (α) = {alpha:.2f}")

    # b. Encontre os valores críticos –z0 e z0 e identifique as regiões de rejeição.
    # Para um teste bilateral, a área em cada cauda é α / 2.
    alpha_over_2 = alpha / 2
    z_critico_left = scipy.stats.norm.ppf(alpha_over_2)
    z_critico_right = scipy.stats.norm.ppf(1 - alpha_over_2)

    print(f"b. Valores Críticos de Z (±z₀):")
    print(f"   -z₀ = {z_critico_left:.2f}")
    print(f"   +z₀ = {z_critico_right:.2f}")
    print(f"   Regiões de Rejeição: Rejeitar H₀ se z < {z_critico_left:.2f} OU z > {z_critico_right:.2f}.")

    # c. Esboce um gráfico. Decida se rejeita a hipótese nula.
    print(f"\nc. Gráfico e Decisão para α = {alpha:.2f}:")
    # Esboço do gráfico (Distribuição Amostral das Médias)
    x_vals = np.linspace(mu_0 - 4 * erro_padrao, mu_0 + 4 * erro_padrao, 500)
    y_vals = scipy.stats.norm.pdf(x_vals, loc=mu_0, scale=erro_padrao)

    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, color='blue', label='Distribuição Amostral das Médias')
    plt.axvline(mu_0, color='gray', linestyle='--', linewidth=0.8, label=f'Média H₀ = ${mu_0}')
    plt.axvline(x_barra, color='green', linestyle='-', label=f'Média Amostral = ${x_barra}')

    # Marcar a estatística de teste z
    # A linha vermelha da estatística de teste será plotada na escala original para facilitar a visualização
    plt.axvline(x_barra, color='purple', linestyle=':', label=f'Estatística de Teste Z = {z_estatistica:.2f}')

    # Sombrear regiões de rejeição
    x_fill_left = np.linspace(x_vals.min(), mu_0 + z_critico_left * erro_padrao, 100)
    y_fill_left = scipy.stats.norm.pdf(x_fill_left, loc=mu_0, scale=erro_padrao)
    plt.fill_between(x_fill_left, 0, y_fill_left, color='salmon', alpha=0.6, label=f'Região de Rejeição (α/2={alpha_over_2:.2f})')

    x_fill_right = np.linspace(mu_0 + z_critico_right * erro_padrao, x_vals.max(), 100)
    y_fill_right = scipy.stats.norm.pdf(x_fill_right, loc=mu_0, scale=erro_padrao)
    plt.fill_between(x_fill_right, 0, y_fill_right, color='salmon', alpha=0.6)

    plt.title(f'Teste de Hipótese para Média (Bilateral, α = {alpha:.2f})')
    plt.xlabel('Custo Anual (US$)')
    plt.ylabel('Densidade de Probabilidade')
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.ticklabel_format(style='plain', axis='x')
    plt.show()

    # Decisão
    if z_estatistica < z_critico_left or z_estatistica > z_critico_right:
        decisao = "Rejeitar H₀"
    else:
        decisao = "Não rejeitar H₀"
    print(f"   Decisão: {decisao}")

    # d. Interprete a decisão no contexto da afirmação original.
    print(f"\nd. Interpretação da decisão para α = {alpha:.2f}:")
    if decisao == "Rejeitar H₀":
        print(f"   Há evidência estatística suficiente em α = {alpha:.2f} para rejeitar a afirmação de que o custo médio anual para criar um filho é de US$ {mu_0}.")
    else:
        print(f"   Não há evidência estatística suficiente em α = {alpha:.2f} para rejeitar a afirmação de que o custo médio anual para criar um filho é de US$ {mu_0}.")