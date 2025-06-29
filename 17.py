import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parâmetros da população
media = 25          # média populacional
desvio_padrao = 1.5        # desvio padrão populacional
n = 50           # tamanho da amostra

# Parâmetros da distribuição amostral
media_sample = media
desvio_padrao_sample = desvio_padrao / np.sqrt(n)

print(f"Média da distribuição amostral: {media_sample}")
print(f"Desvio padrão da distribuição amostral: {desvio_padrao_sample}")

# Criando o eixo x para o gráfico
x = np.linspace(media_sample - 4*desvio_padrao_sample, media_sample + 4*desvio_padrao_sample, 1000)
y = norm.pdf(x, media_sample, desvio_padrao_sample)

# Plotando a distribuição amostral
plt.figure(figsize=(10, 6))
plt.plot(x, y, color='blue', label='Distribuição Amostral das Médias')
plt.title('Distribuição Amostral das Médias (n=64)')
plt.xlabel('Média da Amostra')
plt.ylabel('Densidade de Probabilidade')
plt.axvline(media_sample, color='red', linestyle='--', label=f'Média = {media_sample}')
plt.legend()
plt.grid(True)
plt.show()
