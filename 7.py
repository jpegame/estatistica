#No final do código existe a interpretação dos resultados
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

media = 67 # Velocidade média em milhas por hora
desvio_padrao = 3.5 # Desvio padrão em milhas por hora
z_score = (70 - media) / desvio_padrao

# Calcula a distribuição normal padronizada
x = np.linspace(-4, 4, 1000) # Definição do x para o gráfico
y = norm.pdf(x, 0, 1)  # Distribuição normal padrão (média=0, dp=1)

# Plotando o gráfico
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Distribuição Normal Padrão (Z)', color='blue')

# Pinta a área sob a curva à direita do escore-z
x_fill = np.linspace(z_score, 4, 1000)
y_fill = norm.pdf(x_fill, 0, 1)

area_direita = (1 - norm.cdf(z_score))
plt.fill_between(x_fill, y_fill, color='skyblue', alpha=0.5, label=f'Área à direita = {area_direita:.6f}')

# Linhas auxiliares pra visualização do gráfico
plt.axvline(z_score, color='red', linestyle='--', label=f'z = {z_score:.2f}')
plt.axhline(0, color='black', linewidth=0.5)

plt.title('Curva Normal Padronizada (Z-score)')
plt.xlabel('Score Z')
plt.ylabel('Densidade de Probabilidade')
plt.grid(True)
plt.legend()
plt.show()

# Interpetração dos resultados:
# Existe uma probabilidade de que 19,56% dos veículos estejam acima da velocidade