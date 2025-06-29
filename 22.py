import scipy.stats
import matplotlib.pyplot as plt
import numpy as np

p = 0.58
n = 150
q = 1 - p

x_limite = 100

print(f"Assumindo um tamanho de amostra (n) = {n} adultos para o cálculo da probabilidade.")

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

# b. Calcule a média µ e o desvio padrão σ para a distribuição.
media_normal = np_produto
desvio_padrao_normal = np.sqrt(n * p * q)
print(f"\nb. Média (µ) da distribuição normal: {media_normal:.2f}")
print(f"   Desvio Padrão (σ) da distribuição normal: {desvio_padrao_normal:.2f}")

# c. Aplique a correção de continuidade para reescrever P(x <= 100) e esboce um gráfico.
# P(x <= 100) na distribuição binomial discreta, com correção de continuidade, é P(X <= 100.5).
valor_corrigido = x_limite + 0.5
print(f"\nc. Correção de continuidade: P(x <= {x_limite}) se torna P(X <= {valor_corrigido}) na aproximação normal.")

# Esboço do gráfico
x_vals = np.linspace(media_normal - 4 * desvio_padrao_normal, media_normal + 4 * desvio_padrao_normal, 500)
y_vals = scipy.stats.norm.pdf(x_vals, loc=media_normal, scale=desvio_padrao_normal)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, color='blue', label='Distribuição Normal Aproximada')
plt.axvline(media_normal, color='gray', linestyle='--', linewidth=0.8, label=f'Média = {media_normal:.2f}')
plt.axvline(valor_corrigido, color='red', linestyle='--', label=f'x corrigido = {valor_corrigido}')

# Sombrear a área à esquerda do valor corrigido
x_fill = np.linspace(x_vals.min(), valor_corrigido, 100)
y_fill = scipy.stats.norm.pdf(x_fill, loc=media_normal, scale=desvio_padrao_normal)
plt.fill_between(x_fill, 0, y_fill, color='lightblue', alpha=0.6, label=f'P(x <= {x_limite}) = P(X <= {valor_corrigido})')

plt.title('Aproximação Normal da Distribuição Binomial (n=150, p=0.58)')
plt.xlabel('Número de Adultos que Nunca Usam Capacete')
plt.ylabel('Densidade de Probabilidade')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)
plt.show()

# d. Calcule o correspondente escore-z. (Já feito implicitamente no cálculo)
z_score = (valor_corrigido - media_normal) / desvio_padrao_normal
print(f"\nd. O escore-z correspondente é: {z_score:.2f}")

# e. Use a tabela normal padrão para encontrar a área à esquerda de z e calcule a probabilidade.
probabilidade = scipy.stats.norm.cdf(z_score) # Área à esquerda

print(f"\ne. Área à esquerda de z = {z_score:.2f} é: {probabilidade:.4f}")
print(f"   A probabilidade de que no máximo {x_limite} adultos digam que nunca usam capacete é: {probabilidade:.4f} ou {probabilidade*100:.2f}%")

print("\nInterpretação:")
print(f"A probabilidade de que no máximo 100 dos 150 adultos americanos selecionados aleatoriamente digam que nunca usam capacete ao andar de bicicleta é de aproximadamente {probabilidade*100:.2f}%.")
     