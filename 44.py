import scipy.stats
import matplotlib.pyplot as plt
import numpy as np

z_estatistica = 1.64
nivel_significancia_alpha = 0.10
tipo_teste = "bilateral"

# a. Use a Tabela B.4 do Apêndice B para localizar a área que corresponde a z = 1,64.
area_esquerda_z = scipy.stats.norm.cdf(z_estatistica)
print(f"a. A área que corresponde a z = {z_estatistica} (área à esquerda) é: {area_esquerda_z:.4f}")

# b. Calcule o valor p para um teste bilateral.
# Para um teste bilateral, o p-valor é 2 * P(Z > |z_estatistica|)
# P(Z > |1.64|) = 1 - P(Z < 1.64)
valor_p = 2 * (1 - area_esquerda_z)
print(f"\nb. O valor p para um teste bilateral é: {valor_p:.4f}")

# c. Compare o valor p com alpha e decida se rejeita H0.
print(f"\nc. Comparação:")
print(f"   Valor p = {valor_p:.4f}")
print(f"   Nível de significância (α) = {nivel_significancia_alpha:.2f}")

if valor_p <= nivel_significancia_alpha:
    decisao = "Rejeitar H₀"
    interpretacao = "Há evidência estatística suficiente para rejeitar a hipótese nula."
else:
    decisao = "Não rejeitar H₀"
    interpretacao = "Não há evidência estatística suficiente para rejeitar a hipótese nula."

print(f"\nDecisão: {decisao}")
print(f"Interpretação: {interpretacao}")

# Esboço do gráfico para visualização
x = np.linspace(-4, 4, 500)
y = scipy.stats.norm.pdf(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, color='blue')
plt.axvline(0, color='gray', linestyle='--', linewidth=0.8, label='Média (0)')
plt.axvline(z_estatistica, color='red', linestyle='--', label=f'z = {z_estatistica:.2f}')
plt.axvline(-z_estatistica, color='red', linestyle='--', label=f'z = -{z_estatistica:.2f}')

# Sombrear a área do p-valor (duas caudas)
x_fill_right = np.linspace(z_estatistica, 4, 100)
y_fill_right = scipy.stats.norm.pdf(x_fill_right)
plt.fill_between(x_fill_right, 0, y_fill_right, color='salmon', alpha=0.6, label=f'p-valor/2 = {(valor_p/2):.4f}')

x_fill_left = np.linspace(-4, -z_estatistica, 100)
y_fill_left = scipy.stats.norm.pdf(x_fill_left)
plt.fill_between(x_fill_left, 0, y_fill_left, color='salmon', alpha=0.6)


plt.title(f'Teste Bilateral (z = {z_estatistica:.2f}, α = {nivel_significancia_alpha})')
plt.xlabel('Z-score')
plt.ylabel('Densidade de Probabilidade')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)
plt.show()