import scipy.stats
import matplotlib.pyplot as plt
import numpy as np

media_triglicerideos = 91.4 
desvio_padrao_triglicerideos = 46 / 1.34
desvio_padrao_triglicerideos = round(desvio_padrao_triglicerideos, 2)

# Limites de triglicerídeos de interesse
limite_inferior = 100  # mg/dL
limite_superior = 150  # mg/dL

print(f"Assumindo uma distribuição normal com: ")
print(f"Média ($\mu$) = {media_triglicerideos} mg/dL")
print(f"Desvio Padrão ($\sigma$) = {desvio_padrao_triglicerideos} mg/dL")

# a. Esboce um gráfico.
print("\na. Esboço do gráfico da distribuição normal:")
print(f"A curva em forma de sino representa a distribuição dos níveis de triglicerídeos, centrada em {media_triglicerideos} mg/dL.")
print(f"A área que queremos encontrar é a porção da curva entre {limite_inferior} e {limite_superior} mg/dL.")

# Configuração para o gráfico
x = np.linspace(media_triglicerideos - 4 * desvio_padrao_triglicerideos, media_triglicerideos + 4 * desvio_padrao_triglicerideos, 500)
y = scipy.stats.norm.pdf(x, loc=media_triglicerideos, scale=desvio_padrao_triglicerideos)

plt.figure(figsize=(10, 6))
plt.plot(x, y, color='blue', label='Distribuição do Nível de Triglicerídeos')
plt.axvline(media_triglicerideos, color='gray', linestyle='--', linewidth=0.8, label=f'Média = {media_triglicerideos:.1f} mg/dL')
plt.axvline(limite_inferior, color='red', linestyle='--', label=f'Limite Inferior = {limite_inferior} mg/dL')
plt.axvline(limite_superior, color='green', linestyle='--', label=f'Limite Superior = {limite_superior} mg/dL')

# Sombrear a área entre limite_inferior e limite_superior
x_fill = np.linspace(limite_inferior, limite_superior, 100)
y_fill = scipy.stats.norm.pdf(x_fill, loc=media_triglicerideos, scale=desvio_padrao_triglicerideos)
plt.fill_between(x_fill, 0, y_fill, color='lightgreen', alpha=0.6, label=f'Probabilidade entre {limite_inferior} e {limite_superior} mg/dL')

plt.title('Distribuição dos Níveis de Triglicerídeos nos EUA')
plt.xlabel('Nível de Triglicerídeos (mg/dL)')
plt.ylabel('Densidade de Probabilidade')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)
plt.show()

# b. Calcule os escores-z que correspondem a 100 e 150 mg/dL.
z_inferior = (limite_inferior - media_triglicerideos) / desvio_padrao_triglicerideos
z_superior = (limite_superior - media_triglicerideos) / desvio_padrao_triglicerideos

print(f"\nb. O escore-z para {limite_inferior} mg/dL é: {z_inferior:.2f}")
print(f"O escore-z para {limite_superior} mg/dL é: {z_superior:.2f}")

# c. Encontre a área acumulada para cada escore-z e subtraia a área menor da área maior.
area_acumulada_z_inferior = scipy.stats.norm.cdf(z_inferior)
area_acumulada_z_superior = scipy.stats.norm.cdf(z_superior)

probabilidade_entre_limites = area_acumulada_z_superior - area_acumulada_z_inferior

print(f"\nc. A área acumulada para z = {z_inferior:.2f} é: {area_acumulada_z_inferior:.4f}")
print(f"A área acumulada para z = {z_superior:.2f} é: {area_acumulada_z_superior:.4f}")
print(f"A probabilidade de o nível de triglicerídeo estar entre {limite_inferior} e {limite_superior} mg/dL é: {probabilidade_entre_limites:.4f}")

# d. Interprete os resultados.
print("\nd. Interpretação dos resultados:")
print(f"A probabilidade de uma pessoa selecionada aleatoriamente nos Estados Unidos ter um nível de triglicerídeo entre {limite_inferior} e {limite_superior} mg/dL é de aproximadamente {probabilidade_entre_limites:.4f}, ou {probabilidade_entre_limites*100:.2f}%.")
print(f"Isso significa que cerca de {probabilidade_entre_limites*100:.2f}% da população tem níveis de triglicerídeos nessa faixa, com base nas estimativas de média e desvio padrão usadas.")