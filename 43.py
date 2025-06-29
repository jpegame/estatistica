import scipy.stats
import matplotlib.pyplot as plt
import numpy as np

z_estatistica = -1.71
nivel_significancia_alpha = 0.05
tipo_teste = "unilateral à esquerda"

# a. Use a Tabela para localizar a área que corresponde a z = –1,71.
area_esquerda_z = scipy.stats.norm.cdf(z_estatistica)
print(f"a. A área que corresponde a z = {z_estatistica} (área à esquerda) é: {area_esquerda_z:.4f}")

# b. Obtenha o valor p para um teste unilateral à esquerda, a área na cauda à esquerda.
# Para um teste unilateral à esquerda, o p-valor é a área à esquerda da estatística z.
valor_p = area_esquerda_z
print(f"\nb. O valor p para um teste unilateral à esquerda é: {valor_p:.4f}")

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

# Sombrear a área do p-valor
x_fill = np.linspace(-4, z_estatistica, 100)
y_fill = scipy.stats.norm.pdf(x_fill)
plt.fill_between(x_fill, 0, y_fill, color='skyblue', alpha=0.6, label=f'p-valor = {valor_p:.4f}')

# Adicionar linha para o limite crítico alpha (se relevante, para visualizar a área de rejeição)
# Para um teste unilateral à esquerda com alpha=0.05, o z_critico é norm.ppf(0.05)
z_critico = scipy.stats.norm.ppf(nivel_significancia_alpha)
plt.axvline(z_critico, color='green', linestyle=':', label=f'z_crítico (α={nivel_significancia_alpha}) = {z_critico:.2f}')

plt.title(f'Teste Unilateral à Esquerda (z = {z_estatistica:.2f}, α = {nivel_significancia_alpha})')
plt.xlabel('Z-score')
plt.ylabel('Densidade de Probabilidade')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)
plt.show()