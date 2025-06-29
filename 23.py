import scipy.stats
import matplotlib.pyplot as plt
import numpy as np

p = 0.32
n = 75
q = 1 - p

x_exato = 15

print(f"Probabilidade (p) utilizada para a população geral de homens 50+ = {p*100:.1f}%.")

# a. Determine se você pode usar uma distribuição normal para aproximar a variável binomial.
np_produto = n * p
nq_produto = n * q
pode_aproximar = (np_produto >= 5) and (nq_produto >= 5)

print(f"\na. Verificação da aproximação normal:")
print(f"   np = {np_produto:.2f}")
print(f"   nq = {nq_produto:.2f}")
print(f"   É possível usar uma distribuição normal para aproximar (ambos >= 5)? {'Sim' if pode_aproximar else 'Não'}")

if not pode_aproximar:
    print("   (Não é possível prosseguir com a aproximação normal. O restante da questão assume que sim.)")
    exit() # Interrompe a execução se a aproximação não for válida

# b. Calcule a média µ e o desvio padrão σ para a distribuição normal.
media_normal = np_produto
desvio_padrao_normal = np.sqrt(n * p * q)
print(f"\nb. Média (µ) da distribuição normal: {media_normal:.2f}")
print(f"   Desvio Padrão (σ) da distribuição normal: {desvio_padrao_normal:.2f}")

# c. Calcular os correspondentes escores-z.
# Para "exatamente x", usamos correção de continuidade de (x - 0.5) a (x + 0.5)
x_inferior_corrigido = x_exato - 0.5 # 14.5
x_superior_corrigido = x_exato + 0.5 # 15.5

z_inferior = (x_inferior_corrigido - media_normal) / desvio_padrao_normal
z_superior = (x_superior_corrigido - media_normal) / desvio_padrao_normal
print(f"\nc. Com correção de continuidade, para P(x = {x_exato}) usamos o intervalo [{x_inferior_corrigido}, {x_superior_corrigido}].")
print(f"   O escore-z para {x_inferior_corrigido} é: {z_inferior:.2f}")
print(f"   O escore-z para {x_superior_corrigido} é: {z_superior:.2f}")

# d. Use a tabela normal padrão para encontrar a área à esquerda de cada escore-z e calcule a probabilidade.
area_esquerda_z_inferior = scipy.stats.norm.cdf(z_inferior)
area_esquerda_z_superior = scipy.stats.norm.cdf(z_superior)

probabilidade_exatamente_15 = area_esquerda_z_superior - area_esquerda_z_inferior

print(f"\nd. Área à esquerda de z = {z_inferior:.2f} é: {area_esquerda_z_inferior:.4f}")
print(f"   Área à esquerda de z = {z_superior:.2f} é: {area_esquerda_z_superior:.4f}")
print(f"   A probabilidade de que exatamente {x_exato} digam que sim é: {probabilidade_exatamente_15:.4f} ou {probabilidade_exatamente_15*100:.2f}%")

# Esboço do gráfico (opcional, mas útil para visualização)
x_vals = np.linspace(media_normal - 4 * desvio_padrao_normal, media_normal + 4 * desvio_padrao_normal, 500)
y_vals = scipy.stats.norm.pdf(x_vals, loc=media_normal, scale=desvio_padrao_normal)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, color='blue', label='Distribuição Normal Aproximada')
plt.axvline(media_normal, color='gray', linestyle='--', linewidth=0.8, label=f'Média = {media_normal:.2f}')
plt.axvline(x_inferior_corrigido, color='red', linestyle=':', linewidth=0.8, label=f'Limite Inferior = {x_inferior_corrigido}')
plt.axvline(x_superior_corrigido, color='green', linestyle=':', linewidth=0.8, label=f'Limite Superior = {x_superior_corrigido}')

# Sombrear a área entre os limites corrigidos
x_fill = np.linspace(x_inferior_corrigido, x_superior_corrigido, 100)
y_fill = scipy.stats.norm.pdf(x_fill, loc=media_normal, scale=desvio_padrao_normal)
plt.fill_between(x_fill, 0, y_fill, color='lightcoral', alpha=0.6, label=f'P(x = {x_exato})')

plt.title(f'Aproximação Normal para P(x = {x_exato}) (n=75, p=0.32)')
plt.xlabel('Número de Homens com Artrite')
plt.ylabel('Densidade de Probabilidade')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)
plt.show()

print("\nInterpretação:")
print(f"A probabilidade de que exatamente 15 dos 75 homens selecionados aleatoriamente (com pelo menos 50 anos nos EUA) tenham artrite é de aproximadamente {probabilidade_exatamente_15*100:.2f}%.")
     