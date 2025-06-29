import scipy.stats
import matplotlib.pyplot as plt
import numpy as np

media_populacao = 176800
desvio_padrao_populacao = 50000
tamanho_amostra = 12
preco_medio_alvo = 160000

# a. Use o teorema do limite central para encontrar µx-barra e σx-barra.
media_distribuicao_amostral = media_populacao
desvio_padrao_distribuicao_amostral = desvio_padrao_populacao / np.sqrt(tamanho_amostra)

print(f"a. Média da distribuição amostral das médias (µ_x̄) = US$ {media_distribuicao_amostral:.2f}")
print(f"   Desvio padrão da distribuição amostral das médias (σ_x̄) = US$ {desvio_padrao_distribuicao_amostral:.2f}")

# Esboce a distribuição amostral das médias amostrais.
print("\nEsboço do gráfico da distribuição amostral das médias:")
print("A distribuição amostral das médias é uma curva normal, centrada na média da população, mas é mais estreita do que a distribuição da população original.")

# Configuração para o gráfico
x_amostral = np.linspace(media_distribuicao_amostral - 4 * desvio_padrao_distribuicao_amostral,
                         media_distribuicao_amostral + 4 * desvio_padrao_distribuicao_amostral, 500)
y_amostral = scipy.stats.norm.pdf(x_amostral, loc=media_distribuicao_amostral, scale=desvio_padrao_distribuicao_amostral)

plt.figure(figsize=(10, 6))
plt.plot(x_amostral, y_amostral, color='blue', label=f'Distribuição Amostral (n={tamanho_amostra}, σ_x̄={desvio_padrao_distribuicao_amostral:.2f})')
plt.axvline(media_distribuicao_amostral, color='gray', linestyle='--', linewidth=0.8, label=f'Média (µ_x̄) = US$ {media_distribuicao_amostral:.2f}')

# Adicionar linha para o preço médio alvo
plt.axvline(preco_medio_alvo, color='red', linestyle='--', label=f'x̄ = US$ {preco_medio_alvo:.2f}')

# b. Calcule o escore-z que corresponda a x-barra = US$ 160.000.
z_score = (preco_medio_alvo - media_distribuicao_amostral) / desvio_padrao_distribuicao_amostral
print(f"\nb. O escore-z que corresponde a x̄ = US$ {preco_medio_alvo:.2f} é: {z_score:.2f}")

# c. Encontre a área acumulada que corresponda ao escore-z e calcule a probabilidade.
area_esquerda_z = scipy.stats.norm.cdf(z_score)
probabilidade_maior_que = 1 - area_esquerda_z

print(f"\nc. Área acumulada para z = {z_score:.2f} é: {area_esquerda_z:.4f}")
print(f"   A probabilidade de o preço médio de venda ser maior que US$ {preco_medio_alvo:.2f} é: {probabilidade_maior_que:.4f}")

# Sombrear a área à direita do preço médio alvo no gráfico
x_fill = np.linspace(preco_medio_alvo, media_distribuicao_amostral + 4 * desvio_padrao_distribuicao_amostral, 100)
y_fill = scipy.stats.norm.pdf(x_fill, loc=media_distribuicao_amostral, scale=desvio_padrao_distribuicao_amostral)
plt.fill_between(x_fill, 0, y_fill, color='salmon', alpha=0.6, label=f'Probabilidade > US$ {preco_medio_alvo:.2f}')

plt.title('Distribuição Amostral das Médias de Preços de Venda de Residências')
plt.xlabel('Preço Médio de Venda (US$)')
plt.ylabel('Densidade de Probabilidade')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)
plt.ticklabel_format(style='plain', axis='x') # Para evitar notação científica no eixo x
plt.show()

# d. Interprete os resultados.
print("\nd. Interpretação dos resultados:")
print(f"A probabilidade de que o preço de vendas médio de uma amostra aleatória de {tamanho_amostra} casas seja maior que US$ {preco_medio_alvo:.2f} é de aproximadamente {probabilidade_maior_que:.4f}, ou {probabilidade_maior_que*100:.2f}%.")
print("Isso significa que há uma alta probabilidade de que a média de uma amostra de 12 casas seja superior a US$ 160.000, dada a média populacional e o desvio padrão.")