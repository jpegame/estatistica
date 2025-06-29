import scipy.stats
import matplotlib.pyplot as plt
import numpy as np

mu_0 = 35
n = 100
x_barra = 36
sigma = 4
alpha = 0.05

# a. Identifique a afirmação. Então, formule as hipóteses nula e alternativa.
afirmacao_45 = "A velocidade média de veículos é maior que 35 milhas por hora (μ > 35)."
print(f"a. Afirmação: {afirmacao_45}")

H0_simbolo = "μ ≤ 35"
Ha_simbolo = "μ > 35"
print(f"   H₀: {H0_simbolo} (Hipótese Nula)")
print(f"   Hₐ: {Ha_simbolo} (Hipótese Alternativa - REPRESENTA A AFIRMAÇÃO)")

# b. Identifique o nível de significância α.
print(f"\nb. Nível de significância (α) = {alpha:.2f}")

# c. Calcule a estatística de teste padronizada z.
erro_padrao = sigma / np.sqrt(n)
z_estatistica = (x_barra - mu_0) / erro_padrao
print(f"\nc. Estatística de teste padronizada z = {z_estatistica:.2f}")

# d. Encontre o valor p.
# Para um teste unilateral à direita, o p-valor é a área à direita de z.
valor_p = 1 - scipy.stats.norm.cdf(z_estatistica)
print(f"\nd. Valor p = {valor_p:.4f}")

# e. Decida se rejeita a hipótese nula.
print(f"\ne. Decisão:")
print(f"   Valor p ({valor_p:.4f}) vs α ({alpha:.2f})")
if valor_p <= alpha:
    decisao = "Rejeitar H₀"
else:
    decisao = "Não rejeitar H₀"
print(f"   Decisão: {decisao}")

# f. Interprete a decisão no contexto da afirmação original.
print(f"\nf. Interpretação da decisão:")
if decisao == "Rejeitar H₀":
    print(f"   Há evidência estatística suficiente em α = {alpha:.2f} para apoiar a afirmação de que a velocidade média de veículos que passam pela rua é maior que 35 milhas por hora.")
else:
    print(f"   Não há evidência estatística suficiente em α = {alpha:.2f} para apoiar a afirmação de que a velocidade média de veículos que passam pela rua é maior que 35 milhas por hora.")

# Esboço do gráfico para visualização
x_vals = np.linspace(mu_0 - 3 * erro_padrao, mu_0 + 3 * erro_padrao, 500)
y_vals = scipy.stats.norm.pdf(x_vals, loc=mu_0, scale=erro_padrao)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, color='blue', label='Distribuição Amostral das Médias')
plt.axvline(mu_0, color='gray', linestyle='--', linewidth=0.8, label=f'Média H₀ = {mu_0} mph')
plt.axvline(x_barra, color='green', linestyle='--', label=f'Média Amostral = {x_barra} mph')
plt.axvline(x_barra, color='red', linestyle='--', linewidth=1.5, label=f'z-estatística = {z_estatistica:.2f}')


# Sombrear a área do p-valor
x_fill = np.linspace(x_barra, x_vals.max(), 100)
y_fill = scipy.stats.norm.pdf(x_fill, loc=mu_0, scale=erro_padrao)
plt.fill_between(x_fill, 0, y_fill, color='salmon', alpha=0.6, label=f'p-valor = {valor_p:.4f}')

plt.title('Teste de Hipótese para Média (Unilateral à Direita)')
plt.xlabel('Velocidade (milhas/hora)')
plt.ylabel('Densidade de Probabilidade')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)
plt.show()