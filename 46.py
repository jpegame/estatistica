import scipy.stats
import matplotlib.pyplot as plt
import numpy as np

mu_0 = 3
n = 25
x_barra = 3.3
sigma = 0.5
alpha = 0.01
populacao_normal = True

# a. Identifique a afirmação. Então, estabeleça as hipóteses nula e alternativa.
afirmacao_46 = "O tempo médio para recuperar o custo de uma cirurgia bariátrica é de 3 anos (μ = 3)."
print(f"a. Afirmação: {afirmacao_46}")

H0_simbolo = "μ = 3"
Ha_simbolo = "μ ≠ 3"
print(f"   H₀: {H0_simbolo} (Hipótese Nula - REPRESENTA A AFIRMAÇÃO)")
print(f"   Hₐ: {Ha_simbolo} (Hipótese Alternativa)")

# b. Identifique o nível de significância α.
print(f"\nb. Nível de significância (α) = {alpha:.2f}")

# c. Calcule a estatística de teste padronizada z.
erro_padrao = sigma / np.sqrt(n)
z_estatistica = (x_barra - mu_0) / erro_padrao
print(f"\nc. Estatística de teste padronizada z = {z_estatistica:.2f}")

# d. Encontre o valor p.
# Para um teste bilateral, o p-valor é 2 * P(Z > |z_estatistica|)
valor_p = 2 * (1 - scipy.stats.norm.cdf(abs(z_estatistica)))
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
    print(f"   Há evidência estatística suficiente em α = {alpha:.2f} para duvidar da afirmação de que o tempo médio para recuperar o custo de uma cirurgia bariátrica é de 3 anos.")
else:
    print(f"   Não há evidência estatística suficiente em α = {alpha:.2f} para duvidar da afirmação de que o tempo médio para recuperar o custo de uma cirurgia bariátrica é de 3 anos.")

# Esboço do gráfico para visualização
x_vals = np.linspace(mu_0 - 3 * erro_padrao, mu_0 + 3 * erro_padrao, 500)
y_vals = scipy.stats.norm.pdf(x_vals, loc=mu_0, scale=erro_padrao)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, color='blue', label='Distribuição Amostral das Médias')
plt.axvline(mu_0, color='gray', linestyle='--', linewidth=0.8, label=f'Média H₀ = {mu_0} anos')
plt.axvline(x_barra, color='green', linestyle='--', label=f'Média Amostral = {x_barra} anos')
plt.axvline(x_barra, color='red', linestyle='--', linewidth=1.5, label=f'z-estatística = {z_estatistica:.2f}')


# Sombrear a área do p-valor (duas caudas)
z_abs = abs(z_estatistica)
x_fill_right = np.linspace(mu_0 + z_abs * erro_padrao, x_vals.max(), 100) # Usar mu_0 + z_abs*sigma_x_barra para posicionar
y_fill_right = scipy.stats.norm.pdf(x_fill_right, loc=mu_0, scale=erro_padrao)
plt.fill_between(x_fill_right, 0, y_fill_right, color='salmon', alpha=0.6, label=f'p-valor/2 = {(valor_p/2):.4f}')

x_fill_left = np.linspace(x_vals.min(), mu_0 - z_abs * erro_padrao, 100)
y_fill_left = scipy.stats.norm.pdf(x_fill_left, loc=mu_0, scale=erro_padrao)
plt.fill_between(x_fill_left, 0, y_fill_left, color='salmon', alpha=0.6)


plt.title('Teste de Hipótese para Média (Bilateral)')
plt.xlabel('Tempo (anos)')
plt.ylabel('Densidade de Probabilidade')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)
plt.show()