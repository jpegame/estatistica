import scipy.stats
import matplotlib.pyplot as plt
import numpy as np

alpha_51 = 0.10
n_51 = 9
tipo_teste_51 = "unilateral à direita"

# a. Identifique os graus de liberdade.
df_51 = n_51 - 1 # Graus de liberdade = n - 1
print(f"a. Graus de liberdade (df) = n - 1 = {df_51}")

# b. Use a coluna “unilateral, α” na Tabela para encontrar t0.
t0_51 = scipy.stats.t.ppf(1 - alpha_51, df=df_51)
print(f"b. O valor crítico t₀ para um teste unilateral à direita com α = {alpha_51:.2f} e n = {n_51} (df={df_51}) é: {t0_51:.3f}")

# Gráfico para visualização do valor crítico t0
x_vals_t = np.linspace(-4, 4, 500) # Eixo x para a distribuição t
y_vals_t = scipy.stats.t.pdf(x_vals_t, df=df_51) # PDF da distribuição t

plt.figure(figsize=(8, 5)) # Define o tamanho da figura
plt.plot(x_vals_t, y_vals_t, color='blue', label=f'Distribuição t (df={df_51})') # Plota a curva t
plt.axvline(0, color='gray', linestyle='--', linewidth=0.8, label='Média (0)') # Linha da média
plt.axvline(t0_51, color='red', linestyle='--', label=f't₀ = {t0_51:.3f}') # Linha do valor crítico t0

# Sombrear a região de rejeição (cauda direita)
x_fill_right_t = np.linspace(t0_51, 4, 100)
y_fill_right_t = scipy.stats.t.pdf(x_fill_right_t, df=df_51)
plt.fill_between(x_fill_right_t, 0, y_fill_right_t, color='salmon', alpha=0.6, label=f'Região de Rejeição (α={alpha_51:.2f})')

plt.title(f'Teste Unilateral à Direita (t₀, α = {alpha_51:.2f}, n = {n_51})') # Título do gráfico
plt.xlabel('Estatística t') # Rótulo do eixo X
plt.ylabel('Densidade de Probabilidade') # Rótulo do eixo Y
plt.legend() # Mostra a legenda
plt.grid(True, linestyle=':', alpha=0.7) # Adiciona grade
plt.show() # Exibe o gráfico