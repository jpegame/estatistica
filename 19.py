import scipy.stats 
import matplotlib.pyplot as plt 
import numpy as np

media_populacao = 190
desvio_padrao_populacao = 48
valor_alvo = 200
tamanho_amostra = 10

# a. Obtenha o escore-z que corresponda a x.
z_individual = (valor_alvo - media_populacao) / desvio_padrao_populacao 
print(f"a. O escore-z para um monitor individual de US$ {valor_alvo:.2f} é: {z_individual:.2f}")

# b. Use a tabela normal padrão para encontrar a probabilidade.
prob_individual_menor_que_200 = scipy.stats.norm.cdf(z_individual) 
print(f"b. A probabilidade de um monitor individual custar menos de US$ {valor_alvo:.2f} é: {prob_individual_menor_que_200:.4f}")

# --- Parte 2: Probabilidade para a média de 10 monitores ---
print("\n--- Para a média de 10 monitores de LCD ---")

# a. Obtenha o escore-z que corresponda a x-barra.
media_distribuicao_amostral = media_populacao 
desvio_padrao_distribuicao_amostral = desvio_padrao_populacao / np.sqrt(tamanho_amostra)

z_amostra = (valor_alvo - media_distribuicao_amostral) / desvio_padrao_distribuicao_amostral 
print(f"a. Média da distribuição amostral (µ_x̄) = {desvio_padrao_distribuicao_amostral:.2f}") 
print(f" O escore-z para a média de 10 monitores de US$ {valor_alvo:.2f} é: {z_amostra:.2f}")

# b. Use a tabela normal padrão para encontrar a probabilidade.
prob_amostra_menor_que_200 = scipy.stats.norm.cdf(z_amostra) 
print(f"b. A probabilidade da média de 10 monitores custar menos de US$ {valor_alvo:.2f} é: {prob_amostra_menor_que_200:.4f}")

# --- Parte 3: Comparação das Probabilidades e Gráfico ---
print("\nc. Comparação das probabilidades:") 
print(f"Probabilidade para um monitor individual ( < U$200): {prob_amostra_menor_que_200*100:.2f}%")

print("\nInterpretação da Comparação:") 
print("A probabilidade de um monitor individual custar menos de U$ 200.") 
print("Isso ocorre porque a distribuição amostral das médias (para n=10) é mais estreita (tem um desvio padrão menor) do que a distribuição da população original.") 
print("Com uma distribuição mais concentrada em torno da média, é mais provável que a média de uma amostra esteja próxima da média populacional, e menos provável que ela se desvie para valores extremos.") 
print("Como USáé190), a distribuição amostral concentra mais de sua probabilidade nessa região, tornando a probabilidade acumulada até 200 maior para a média da amostra.")

# Gerar valores x para ambas as curvas
x_vals_individual = np.linspace(media_populacao - 3 * desvio_padrao_populacao, media_populacao + 3 * desvio_padrao_populacao, 500) 
y_vals_individual = scipy.stats.norm.pdf(x_vals_individual, loc=media_populacao, scale=desvio_padrao_populacao)

x_vals_amostra = np.linspace(media_distribuicao_amostral - 3 * desvio_padrao_distribuicao_amostral, media_distribuicao_amostral + 3 * desvio_padrao_distribuicao_amostral, 500) 
y_vals_amostra = scipy.stats.norm.pdf(x_vals_amostra, loc=media_distribuicao_amostral, scale=desvio_padrao_distribuicao_amostral)

plt.figure(figsize=(12, 7)) 
plt.plot(x_vals_individual, y_vals_individual, color='skyblue', label='Distribuição Individual (σ=48)', linestyle='--', alpha=0.7) 
plt.plot(x_vals_amostra, y_vals_amostra, color='blue', label=f'Distribuição Amostral (n={tamanho_amostra}, σ_x̄={desvio_padrao_distribuicao_amostral:.2f})')

plt.axvline(media_populacao, color='gray', linestyle=':', linewidth=0.8, label=f'Média (µ) = U$ {valor_alvo}')

# Sombrear área para o individual
x_fill_ind = np.linspace(x_vals_individual.min(), valor_alvo, 100) 
y_fill_ind = scipy.stats.norm.pdf(x_fill_ind, loc=media_populacao, scale=desvio_padrao_populacao) 
plt.fill_between(x_fill_ind, 0, y_fill_ind, color='lightblue', alpha=0.3, label=f'Prob. Individual < {valor_alvo} ({prob_individual_menor_que_200*100:.2f}%)')

# Sombrear área para a média da amostra
x_fill_amostra = np.linspace(x_vals_amostra.min(), valor_alvo, 100) 
y_fill_amostra = scipy.stats.norm.pdf(x_fill_amostra, loc=media_distribuicao_amostral, scale=desvio_padrao_distribuicao_amostral) 
plt.fill_between(x_fill_amostra, 0, y_fill_amostra, color='lightgreen', alpha=0.3, label=f'Prob. Média Amostra < {valor_alvo} ({prob_amostra_menor_que_200*100:.2f}%)')

plt.title('Comparação das Probabilidades de Custo de Monitores de LCD') 
plt.xlabel('Custo (US$)') 
plt.ylabel('Densidade de Probabilidade') 
plt.legend() 
plt.grid(True, linestyle=':', alpha=0.7) 
plt.show()