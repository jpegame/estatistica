#No final do código existe a interpretação dos resultados
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

media = 45 # Tempo na loja em minutos
desvio_padrao = 12 # Desvio padrão em minutos
z_score_1 = (33 - media) / desvio_padrao
z_score_2 = (66 - media) / desvio_padrao

# Calcula a distribuição normal padronizada
x = np.linspace(-4, 4, 1000) # Definição do x para o gráfico
y = norm.pdf(x, 0, 1)  # Distribuição normal padrão (média=0, dp=1)

# Plotando o gráfico
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Distribuição Normal Padrão (Z)', color='blue')

# Pinta a área sob a curva à entre os dois escores-z
x_fill = np.linspace(z_score_1, z_score_2, 1000)
y_fill = norm.pdf(x_fill, 0, 1)

area_1 = norm.cdf(z_score_1)
area_2 = norm.cdf(z_score_2)

# Garante que a área seja positiva
if area_1 > area_2:
    area = area_1 - area_2
else:
    area = area_2 - area_1

plt.fill_between(x_fill, y_fill, color='skyblue', alpha=0.5, label=f'Área = {area:.6f}')

# Linhas auxiliares pra visualização do gráfico
plt.axvline(z_score_1, color='red', linestyle='--', label=f'z = {z_score_1:.2f}')
plt.axvline(z_score_2, color='red', linestyle='--', label=f'z = {z_score_2:.2f}')
plt.axhline(0, color='black', linewidth=0.5)

plt.title('Curva Normal Padronizada (Z-score)')
plt.xlabel('Score Z')
plt.ylabel('Densidade de Probabilidade')
plt.grid(True)
plt.legend()
plt.show()

# Interpetração dos resultados:
# Existe uma probabilidade de que 80.12% dos consumidores estejam na loja entre 33 e 60min,
# logo levando em conta que 150 consumidores entrem na loja, em torno de 120 permaneceriam nessa margem