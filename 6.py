import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Valores dos escores-z
z_score_1 = -2.165
z_score_2 = -1.35

# Criação da função densidade da curva normal padrão
x = np.linspace(-4, 4, 1000)
y = norm.pdf(x, 0, 1)

# Cria o gráfico
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Curva Normal Padrão', color='blue')

# Pinta a área sob a curva à entre os dois escores-z
x_fill = np.linspace(z_score_1, z_score_2, 1000)
y_fill = norm.pdf(x_fill, 0, 1)
plt.fill_between(x_fill, y_fill, color='skyblue', alpha=0.5, label=f'Área sombreada')

# Linhas auxiliares pra visualização do gráfico
plt.axvline(z_score_1, color='red', linestyle='--', label=f'z = {z_score_1}')
plt.axvline(z_score_2, color='red', linestyle='--', label=f'z = {z_score_2}')
plt.axhline(0, color='black', linewidth=0.5)

# Ajustes do layout
plt.title('Curva Normal Padrão')
plt.legend()
plt.grid(True)

# Mostrar a área acumulada até z, o valor da área mostra no gráfico
area_1 = norm.cdf(z_score_1)
area_2 = norm.cdf(z_score_2)
plt.text(z_score_1 - 0.05, 0.1, f'Área = {area_1:.6f}', ha='right', color='black')
plt.text(z_score_2 + 0.05, 0.1, f'Área = {(1 - area_2):.6f}', ha='left', color='black')
plt.show()
