import scipy.stats
import matplotlib.pyplot as plt
import numpy as np

alpha_52 = 0.05
n_52 = 16
tipo_teste_52 = "bilateral"

# a. Identifique os graus de liberdade.
df_52 = n_52 - 1 # Graus de liberdade = n - 1
print(f"a. Graus de liberdade (df) = n - 1 = {df_52}")

# b. Use a coluna “bilateral, α” na Tabela para encontrar –t0 e t0.
# Para um teste bilateral, a área em cada cauda é α / 2.
alpha_over_2_52 = alpha_52 / 2
# t0_left é o valor t que tem α/2 de área à sua esquerda.
t0_52_left = scipy.stats.t.ppf(alpha_over_2_52, df=df_52)
# t0_right é o valor t que tem 1 - α/2 de área à sua esquerda.
t0_52_right = scipy.stats.t.ppf(1 - alpha_over_2_52, df=df_52)

print(f"b. Os valores críticos t₀ para um teste bilateral com α = {alpha_52:.2f} e n = {n_52} (df={df_52}) são:")
print(f"   -t₀ = {t0_52_left:.3f}")
print(f"   +t₀ = {t0_52_right:.3f}")

# Gráfico para visualização dos valores críticos t0
x_vals_t_bilateral = np.linspace(-4, 4, 500) # Eixo x para a distribuição t
y_vals_t_bilateral = scipy.stats.t.pdf(x_vals_t_bilateral, df=df_52) # PDF da distribuição t

plt.figure(figsize=(8, 5)) # Define o tamanho da figura
plt.plot(x_vals_t_bilateral, y_vals_t_bilateral, color='blue', label=f'Distribuição t (df={df_52})') # Plota a curva t
plt.axvline(0, color='gray', linestyle='--', linewidth=0.8, label='Média (0)') # Linha da média
plt.axvline(t0_52_left, color='red', linestyle='--', label=f't₀_L = {t0_52_left:.3f}') # Linha do valor crítico t0 esquerdo
plt.axvline(t0_52_right, color='red', linestyle='--', label=f't₀_R = {t0_52_right:.3f}') # Linha do valor crítico t0 direito

# Sombrear as regiões de rejeição (duas caudas)
# Cauda esquerda
x_fill_left_t = np.linspace(-4, t0_52_left, 100)
y_fill_left_t = scipy.stats.t.pdf(x_fill_left_t, df=df_52)
plt.fill_between(x_fill_left_t, 0, y_fill_left_t, color='salmon', alpha=0.6, label=f'Região de Rejeição (α/2={alpha_over_2_52:.3f})')

# Cauda direita
x_fill_right_t = np.linspace(t0_52_right, 4, 100)
y_fill_right_t = scipy.stats.t.pdf(x_fill_right_t, df=df_52)
plt.fill_between(x_fill_right_t, 0, y_fill_right_t, color='salmon', alpha=0.6)

plt.title(f'Teste Bilateral (t₀, α = {alpha_52:.2f}, n = {n_52})') # Título do gráfico
plt.xlabel('Estatística t') # Rótulo do eixo X
plt.ylabel('Densidade de Probabilidade') # Rótulo do eixo Y
plt.legend() # Mostra a legenda
plt.grid(True, linestyle=':', alpha=0.7) # Adiciona grade
plt.show() # Exibe o gráfico