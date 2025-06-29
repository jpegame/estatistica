import scipy.stats
import matplotlib.pyplot as plt
import numpy as np

print("--- Questão 14 ---")

media_tempo = 11.2 
desvio_padrao_tempo = 2.1
percentil_corte = 0.10

# a. Esboce um gráfico da distribuição normal.
print("\na. Esboço do gráfico da distribuição normal:")
print(f"A curva representa a distribuição do tempo de trabalho dos funcionários, centrada em {media_tempo} anos.")
print(f"Queremos encontrar o tempo máximo que define o limite inferior de {percentil_corte*100:.0f}% da distribuição.")

x = np.linspace(media_tempo - 4 * desvio_padrao_tempo, media_tempo + 4 * desvio_padrao_tempo, 500)
y = scipy.stats.norm.pdf(x, loc=media_tempo, scale=desvio_padrao_tempo)

plt.figure(figsize=(10, 6)) # Define o tamanho da figura para melhor visualização
plt.plot(x, y, color='blue', label='Distribuição do Tempo de Trabalho') # Plota a curva da distribuição

# Adicionar uma linha vertical para a média da distribuição
plt.axvline(media_tempo, color='gray', linestyle='--', linewidth=0.8, label=f'Média = {media_tempo} anos')

# b. Determine o escore-z que corresponda à área dada.
z_score_corte = scipy.stats.norm.ppf(percentil_corte)
print(f"\nb. O escore-z que corresponde ao percentil {percentil_corte*100:.0f}% é: {z_score_corte:.2f}")

# c. Calcule x usando a fórmula x = µ + zσ.
# Esta fórmula converte um z-score de volta para a escala original de dados (tempo em anos).
tempo_maximo_corte = media_tempo + z_score_corte * desvio_padrao_tempo
print(f"c. O tempo máximo de trabalho para ser cortado é: {tempo_maximo_corte:.2f} anos")

# Adicionar uma linha vertical no gráfico para o tempo máximo de corte calculado
plt.axvline(tempo_maximo_corte, color='red', linestyle='--', label=f'Limite de Corte (10%) = {tempo_maximo_corte:.2f} anos')

# Sombrear a área no gráfico que representa os 10% com menos tempo na empresa
# Cria um novo array x_fill apenas para a área que será sombreada (do extremo esquerdo até o limite de corte)
x_fill = np.linspace(media_tempo - 4 * desvio_padrao_tempo, tempo_maximo_corte, 100)
# Calcula os valores y correspondentes para essa seção da curva
y_fill = scipy.stats.norm.pdf(x_fill, loc=media_tempo, scale=desvio_padrao_tempo)
# Preenche a área entre a curva e o eixo x
plt.fill_between(x_fill, 0, y_fill, color='purple', alpha=0.6, label=f'{percentil_corte*100:.0f}% com menos tempo')

plt.title('Distribuição do Tempo de Trabalho e Limite de Corte') # Título do gráfico
plt.xlabel('Tempo de Trabalho (anos)') # Rótulo do eixo X
plt.ylabel('Densidade de Probabilidade') # Rótulo do eixo Y
plt.legend() # Exibe a legenda do gráfico
plt.grid(True, linestyle=':', alpha=0.7) # Adiciona uma grade
plt.show() # Exibe o gráfico

# d. Interprete o resultado.
print("\nd. Interpretação do resultado:")
print(f"O tempo máximo que um funcionário pode ter trabalhado na empresa e ainda assim ser cortado (pertencer aos 10% com menos tempo) é de {tempo_maximo_corte:.2f} anos.")
print(f"Isso significa que qualquer funcionário com um tempo de trabalho igual ou inferior a {tempo_maximo_corte:.2f} anos (com base nos dados fornecidos) seria demitido nesta redução de quadro.")