import scipy.stats
import matplotlib.pyplot as plt
import numpy as np

mu_0 = 1200
n = 7
x_barra = 1125
s = 55
alpha = 0.10
populacao_normal = True

# a. Identifique a afirmação e formule H0 e Ha.
afirmacao_53 = "O custo médio do seguro do sedan de dois anos é menor que US$ 1.200 (μ < 1200)."
print(f"a. Afirmação: {afirmacao_53}")

H0_simbolo = "μ ≥ 1200"
Ha_simbolo = "μ < 1200" # A afirmação do agente
print(f"   H₀: {H0_simbolo} (Hipótese Nula)")
print(f"   Hₐ: {Ha_simbolo} (Hipótese Alternativa - REPRESENTA A AFIRMAÇÃO)")
print("   Tipo de Teste: Unilateral à esquerda")

# b. Identifique o nível de significância α e os graus de liberdade.
df = n - 1 # Graus de liberdade
print(f"\nb. Nível de Significância (α) = {alpha:.2f}")
print(f"   Graus de Liberdade (df) = n - 1 = {df}")

# c. Encontre o valor crítico t0 e identifique a região de rejeição.
# Para um teste unilateral à esquerda, t0 é o valor t que deixa α de área à sua esquerda.
t0_53 = scipy.stats.t.ppf(alpha, df=df)
print(f"\nc. Valor crítico t₀ = {t0_53:.3f}")
print(f"   Região de Rejeição: Rejeitar H₀ se a estatística de teste t < {t0_53:.3f}.")

# d. Calcule a estatística de teste padronizada t. Esboce um gráfico.
erro_padrao_amostral = s / np.sqrt(n) # s / sqrt(n) é o erro padrão amostral
t_estatistica = (x_barra - mu_0) / erro_padrao_amostral
print(f"\nd. Estatística de teste padronizada t = {t_estatistica:.2f}")

# Esboço do gráfico da distribuição t
x_vals_t = np.linspace(-4, 4, 500) # Eixo x para a distribuição t
y_vals_t = scipy.stats.t.pdf(x_vals_t, df=df) # PDF da distribuição t

plt.figure(figsize=(10, 6)) # Define o tamanho da figura
plt.plot(x_vals_t, y_vals_t, color='blue', label=f'Distribuição t (df={df})') # Plota a curva t
plt.axvline(0, color='gray', linestyle='--', linewidth=0.8, label='Média (0)') # Linha da média
plt.axvline(t0_53, color='red', linestyle='--', label=f't₀ = {t0_53:.3f}') # Linha do valor crítico t0
plt.axvline(t_estatistica, color='green', linestyle=':', label=f'Estatística de Teste t = {t_estatistica:.2f}') # Linha da estatística de teste

# Sombrear a região de rejeição (cauda esquerda)
x_fill_left_t = np.linspace(-4, t0_53, 100)
y_fill_left_t = scipy.stats.t.pdf(x_fill_left_t, df=df)
plt.fill_between(x_fill_left_t, 0, y_fill_left_t, color='salmon', alpha=0.6, label=f'Região de Rejeição (α={alpha:.2f})')

plt.title(f'Teste de Hipótese para Média (Unilateral à Esquerda, α = {alpha:.2f})') # Título do gráfico
plt.xlabel('Estatística t') # Rótulo do eixo X
plt.ylabel('Densidade de Probabilidade') # Rótulo do eixo Y
plt.legend() # Mostra a legenda
plt.grid(True, linestyle=':', alpha=0.7) # Adiciona grade
plt.show() # Exibe o gráfico

# e. Decida se rejeita a hipótese nula.
print(f"\ne. Decisão:")
if t_estatistica < t0_53: # Se a estatística de teste cair na região de rejeição
    decisao = "Rejeitar H₀"
else:
    decisao = "Não rejeitar H₀"
print(f"   Decisão: {decisao}")

# f. Interprete a decisão no contexto da afirmação original.
print(f"\nf. Interpretação da decisão:")
if decisao == "Rejeitar H₀":
    print(f"   Há evidência estatística suficiente em α = {alpha:.2f} para concordar com a afirmação do agente de que o custo médio do seguro do sedan de dois anos é menor que US$ {mu_0}.")
else:
    print(f"   Não há evidência estatística suficiente em α = {alpha:.2f} para concordar com a afirmação do agente de que o custo médio do seguro do sedan de dois anos é menor que US$ {mu_0}.")