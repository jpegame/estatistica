import scipy.stats
import matplotlib.pyplot as plt
import numpy as np

alpha = 0.10
tipo_teste = "unilateral à esquerda"

# a. Desenhe o gráfico da curva normal padrão.
print(f"a. Gráfico da curva normal padrão com área α={alpha:.2f} na cauda esquerda.")
x = np.linspace(-4, 4, 500)
y = scipy.stats.norm.pdf(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, color='blue')
plt.axvline(0, color='gray', linestyle='--', linewidth=0.8, label='Média (0)')

# b. Use a Tabela para encontrar a área que esteja mais próxima a α.
# c. Encontre o escore-z que corresponde a essa área. (Este é o valor crítico zc)
# Para um teste unilateral à esquerda, o zc é o valor que deixa 'alpha' de área à sua esquerda.
zc_47 = scipy.stats.norm.ppf(alpha)
print(f"b. A área à esquerda de z = {zc_47:.2f} é: {alpha:.2f}")
print(f"c. O escore-z crítico (zc) é: {zc_47:.2f}")

# Sombrear a região de rejeição
x_rejeicao = np.linspace(-4, zc_47, 100)
y_rejeicao = scipy.stats.norm.pdf(x_rejeicao)
plt.fill_between(x_rejeicao, 0, y_rejeicao, color='red', alpha=0.6, label=f'Região de Rejeição (α={alpha:.2f})')
plt.axvline(zc_47, color='red', linestyle='--', label=f'z_c = {zc_47:.2f}')

plt.title(f'Teste Unilateral à Esquerda (α = {alpha:.2f})')
plt.xlabel('Z-score')
plt.ylabel('Densidade de Probabilidade')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)
plt.show()

# d. Identifique a região de rejeição.
print(f"\nd. Região de Rejeição: Rejeitar H₀ se a estatística de teste z < {zc_47:.2f}.")