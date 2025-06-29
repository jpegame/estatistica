import scipy.stats
import matplotlib.pyplot as plt
import numpy as np

alpha = 0.08
tipo_teste = "bilateral"

# a. Desenhe o gráfico da curva normal padrão.
print(f"a. Gráfico da curva normal padrão com área ½α em cada cauda (α={alpha:.2f}).")
x = np.linspace(-4, 4, 500)
y = scipy.stats.norm.pdf(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, color='blue')
plt.axvline(0, color='gray', linestyle='--', linewidth=0.8, label='Média (0)')

# b. Use a Tabela para encontrar as áreas.
# c. Encontre os escores-z que correspondam a essas áreas. (Valores críticos zc)
alpha_over_2 = alpha / 2
zc_left_48 = scipy.stats.norm.ppf(alpha_over_2)
zc_right_48 = scipy.stats.norm.ppf(1 - alpha_over_2)

print(f"b. Área à esquerda de z_L = {alpha_over_2:.3f}")
print(f"   Área à esquerda de z_R = {1 - alpha_over_2:.3f}")
print(f"c. O escore-z crítico esquerdo (z_L) é: {zc_left_48:.2f}")
print(f"   O escore-z crítico direito (z_R) é: {zc_right_48:.2f}")

# Sombrear as regiões de rejeição
x_rejeicao_left = np.linspace(-4, zc_left_48, 100)
y_rejeicao_left = scipy.stats.norm.pdf(x_rejeicao_left)
plt.fill_between(x_rejeicao_left, 0, y_rejeicao_left, color='red', alpha=0.6, label=f'Região de Rejeição (½α={alpha_over_2:.3f})')

x_rejeicao_right = np.linspace(zc_right_48, 4, 100)
y_rejeicao_right = scipy.stats.norm.pdf(x_rejeicao_right)
plt.fill_between(x_rejeicao_right, 0, y_rejeicao_right, color='red', alpha=0.6)

plt.axvline(zc_left_48, color='red', linestyle='--', label=f'z_L = {zc_left_48:.2f}')
plt.axvline(zc_right_48, color='red', linestyle='--', label=f'z_R = {zc_right_48:.2f}')

plt.title(f'Teste Bilateral (α = {alpha:.2f})')
plt.xlabel('Z-score')
plt.ylabel('Densidade de Probabilidade')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)
plt.show()

# d. Identifique as regiões de rejeição.
print(f"\nd. Região de Rejeição: Rejeitar H₀ se a estatística de teste z < {zc_left_48:.2f} OU se z > {zc_right_48:.2f}.")