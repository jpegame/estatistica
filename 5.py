import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Valor do escore-z
z_score = -2.16

# Criação da função densidade da curva normal padrão
x = np.linspace(-4, 4, 1000)
y = norm.pdf(x, 0, 1)

# Cria o gráfico
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Curva Normal Padrão', color='blue')

# Pinta a área sob a curva à esquerda do escore-z
x_fill = np.linspace(-4, z_score, 1000)
y_fill = norm.pdf(x_fill, 0, 1)
plt.fill_between(x_fill, y_fill, color='skyblue', alpha=0.5, label=f'Área até z = {z_score}')

# Linhas auxiliares pra visualização do gráfico
plt.axvline(z_score, color='red', linestyle='--', label=f'z = {z_score}')
plt.axhline(0, color='black', linewidth=0.5)

# Ajustes do layout
plt.title('Curva Normal Padrão')
plt.legend()
plt.grid(True)

# Mostrar a área acumulada até z, o valor da área mostra no gráfico
area = norm.cdf(z_score)
plt.text(z_score - 0.05, 0.1, f'Área à esquerda = {area:.6f}', ha='right', color='black')
plt.text(z_score + 0.05, 0.1, f'Área à direita = {(1 - area):.6f}', ha='left', color='black')
plt.show()
