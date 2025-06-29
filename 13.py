import scipy.stats
import matplotlib.pyplot as plt
import numpy as np

# Dados fornecidos
media_frenagem = 129     # pés (µ)
desvio_padrao_frenagem = 5.18 # pés (σ)
percentil_desejado = 0.01 # 1% mais baixo

# a. Configuração para o gráfico
x = np.linspace(media_frenagem - 4 * desvio_padrao_frenagem, media_frenagem + 4 * desvio_padrao_frenagem, 500)
y = scipy.stats.norm.pdf(x, loc=media_frenagem, scale=desvio_padrao_frenagem)

plt.figure(figsize=(10, 6))
plt.plot(x, y, color='blue', label='Distribuição de Distâncias de Frenagem')
plt.axvline(media_frenagem, color='gray', linestyle='--', linewidth=0.8, label=f'Média = {media_frenagem} pés')

# b. Encontre o escore-z que corresponda à área dada.
z_score_percentil = scipy.stats.norm.ppf(percentil_desejado)
print(f"\nb. O escore-z que corresponde ao percentil {percentil_desejado*100:.0f}% é: {z_score_percentil:.2f}")

# c. Calcule x usando a fórmula x = µ + zσ.
distancia_frenagem_limite = media_frenagem + z_score_percentil * desvio_padrao_frenagem
print(f"c. A distância de frenagem correspondente é: {distancia_frenagem_limite:.2f} pés")

# Adicionar linha vertical para o limite calculado e sombrear a área
plt.axvline(distancia_frenagem_limite, color='red', linestyle='--', label=f'Limite Inferior de 1% = {distancia_frenagem_limite:.2f} pés')
x_fill = np.linspace(media_frenagem - 4 * desvio_padrao_frenagem, distancia_frenagem_limite, 100)
y_fill = scipy.stats.norm.pdf(x_fill, loc=media_frenagem, scale=desvio_padrao_frenagem)
plt.fill_between(x_fill, 0, y_fill, color='purple', alpha=0.6, label=f'1% mais baixo')

plt.title('Distribuição das Distâncias de Frenagem')
plt.xlabel('Distância de Frenagem (pés)')
plt.ylabel('Densidade de Probabilidade')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)
plt.show()

print("\nd. Interpretação do resultado:")
print(f"A maior distância de frenagem que um desses carros poderia ter e ainda estar no grupo do 1% mais baixo é de {distancia_frenagem_limite:.2f} pés.")
print("Isso significa que 1% dos carros testados teriam uma distância de frenagem igual ou inferior a 116.03 pés (com base nos dados fornecidos), indicando um desempenho de frenagem excepcionalmente bom (menor distância = melhor).")