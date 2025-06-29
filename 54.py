import scipy.stats
import matplotlib.pyplot as plt
import numpy as np

mu_0_ph = 6.8
n_ph = 39
x_barra_ph = 6.7
s_ph = 0.35
alpha_ph = 0.05

# a. Identifique a afirmação e formule H0 e Ha.
afirmacao_ph = "O nível médio do pH da água é de 6,8 (μ = 6,8)."
print(f"a. Afirmação: {afirmacao_ph}")

H0_simbolo_ph = "μ = 6.8"
Ha_simbolo_ph = "μ ≠ 6.8"
print(f"   H₀: {H0_simbolo_ph} (Hipótese Nula - REPRESENTA A AFIRMAÇÃO)")
print(f"   Hₐ: {Ha_simbolo_ph} (Hipótese Alternativa)")
print("   Tipo de Teste: Bilateral")

# b. Identifique o nível de significância α e os graus de liberdade.
df_ph = n_ph - 1 # Graus de liberdade
print(f"\nb. Nível de Significância (α) = {alpha_ph:.2f}")
print(f"   Graus de Liberdade (df) = {df_ph}")

# c. Encontre os valores críticos –t0 e t0 e identifique as regiões de rejeição.
alpha_over_2_ph = alpha_ph / 2
t0_ph_left = scipy.stats.t.ppf(alpha_over_2_ph, df=df_ph)
t0_ph_right = scipy.stats.t.ppf(1 - alpha_over_2_ph, df=df_ph)
print(f"\nc. Valores críticos t₀: -t₀ = {t0_ph_left:.3f}, +t₀ = {t0_ph_right:.3f}")
print(f"   Região de Rejeição: Rejeitar H₀ se t < {t0_ph_left:.3f} OU t > {t0_ph_right:.3f}.")

# d. Calcule a estatística de teste padronizada t. Esboce um gráfico.
erro_padrao_amostral_ph = s_ph / np.sqrt(n_ph)
t_estatistica_ph = (x_barra_ph - mu_0_ph) / erro_padrao_amostral_ph
print(f"\nd. Estatística de teste t = {t_estatistica_ph:.2f}")

# Esboço do gráfico
x_vals_t_ph = np.linspace(-4, 4, 500)
y_vals_t_ph = scipy.stats.t.pdf(x_vals_t_ph, df=df_ph)

plt.figure(figsize=(10, 6))
plt.plot(x_vals_t_ph, y_vals_t_ph, color='blue', label=f'Distribuição t (df={df_ph})')
plt.axvline(0, color='gray', linestyle='--', linewidth=0.8, label='Média (0)')
plt.axvline(t0_ph_left, color='red', linestyle='--', label=f't₀_L = {t0_ph_left:.3f}')
plt.axvline(t0_ph_right, color='red', linestyle='--', label=f't₀_R = {t0_ph_right:.3f}')
plt.axvline(t_estatistica_ph, color='green', linestyle=':', label=f'Estatística de Teste t = {t_estatistica_ph:.2f}')

x_fill_left_ph = np.linspace(-4, t0_ph_left, 100)
y_fill_left_ph = scipy.stats.t.pdf(x_fill_left_ph, df=df_ph)
plt.fill_between(x_fill_left_ph, 0, y_fill_left_ph, color='salmon', alpha=0.6, label=f'Região de Rejeição (α/2={alpha_over_2_ph:.3f})')
x_fill_right_ph = np.linspace(t0_ph_right, 4, 100)
y_fill_right_ph = scipy.stats.t.pdf(x_fill_right_ph, df=df_ph)
plt.fill_between(x_fill_right_ph, 0, y_fill_right_ph, color='salmon', alpha=0.6)

plt.title(f'Teste de Hipótese para Nível de pH (Bilateral, α = {alpha_ph:.2f})')
plt.xlabel('Estatística t')
plt.ylabel('Densidade de Probabilidade')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)
plt.show()

# e. Decida se rejeita a hipótese nula.
print(f"\ne. Decisão:")
if t_estatistica_ph < t0_ph_left or t_estatistica_ph > t0_ph_right:
    decisao_ph = "Rejeitar H₀"
else:
    decisao_ph = "Não rejeitar H₀"
print(f"   Decisão: {decisao_ph}")

# f. Interprete a decisão no contexto da afirmação original.
print(f"\nf. Interpretação da decisão:")
if decisao_ph == "Rejeitar H₀":
    print(f"   Há evidência estatística suficiente em α = {alpha_ph:.2f} para rejeitar a afirmação da indústria de que o nível médio do pH da água no rio é de {mu_0_ph}.")
else:
    print(f"   Não há evidência estatística suficiente em α = {alpha_ph:.2f} para rejeitar a afirmação da indústria de que o nível médio do pH da água no rio é de {mu_0_ph}.")


# --- Teste 2: Condutividade Média do Rio ---
print("\n" + "="*60 + "\n") # Separador
print("--- Questão 54 - Teste 2: Condutividade Média do Rio ---")

# Dados fornecidos
mu_0_cond = 1890 # mg/l (Média hipotética da H0)
n_cond = 39      # Tamanho da amostra
x_barra_cond = 2350 # mg/l (Média amostral)
s_cond = 900     # mg/l (Desvio padrão amostral)
alpha_cond = 0.01  # Nível de significância

# a. Identifique a afirmação e formule H0 e Ha.
afirmacao_cond = "A condutividade média do rio é de 1.890 mg/l (μ = 1890 mg/l)."
print(f"a. Afirmação: {afirmacao_cond}")

H0_simbolo_cond = "μ = 1890"
Ha_simbolo_cond = "μ ≠ 1890"
print(f"   H₀: {H0_simbolo_cond} (Hipótese Nula - REPRESENTA A AFIRMAÇÃO)")
print(f"   Hₐ: {Ha_simbolo_cond} (Hipótese Alternativa)")
print("   Tipo de Teste: Bilateral")

# b. Identifique o nível de significância α e os graus de liberdade.
df_cond = n_cond - 1 # Graus de liberdade
print(f"\nb. Nível de Significância (α) = {alpha_cond:.2f}")
print(f"   Graus de Liberdade (df) = {df_cond}")

# c. Encontre os valores críticos –t0 e t0 e identifique as regiões de rejeição.
alpha_over_2_cond = alpha_cond / 2
t0_cond_left = scipy.stats.t.ppf(alpha_over_2_cond, df=df_cond)
t0_cond_right = scipy.stats.t.ppf(1 - alpha_over_2_cond, df=df_cond)
print(f"\nc. Valores críticos t₀: -t₀ = {t0_cond_left:.3f}, +t₀ = {t0_cond_right:.3f}")
print(f"   Região de Rejeição: Rejeitar H₀ se t < {t0_cond_left:.3f} OU t > {t0_cond_right:.3f}.")

# d. Calcule a estatística de teste padronizada t. Esboce um gráfico.
erro_padrao_amostral_cond = s_cond / np.sqrt(n_cond)
t_estatistica_cond = (x_barra_cond - mu_0_cond) / erro_padrao_amostral_cond
print(f"\nd. Estatística de teste t = {t_estatistica_cond:.2f}")

# Esboço do gráfico
x_vals_t_cond = np.linspace(-4, 4, 500)
y_vals_t_cond = scipy.stats.t.pdf(x_vals_t_cond, df=df_cond)

plt.figure(figsize=(10, 6))
plt.plot(x_vals_t_cond, y_vals_t_cond, color='blue', label=f'Distribuição t (df={df_cond})')
plt.axvline(0, color='gray', linestyle='--', linewidth=0.8, label='Média (0)')
plt.axvline(t0_cond_left, color='red', linestyle='--', label=f't₀_L = {t0_cond_left:.3f}')
plt.axvline(t0_cond_right, color='red', linestyle='--', label=f't₀_R = {t0_cond_right:.3f}')
plt.axvline(t_estatistica_cond, color='green', linestyle=':', label=f'Estatística de Teste t = {t_estatistica_cond:.2f}')

x_fill_left_cond = np.linspace(-4, t0_cond_left, 100)
y_fill_left_cond = scipy.stats.t.pdf(x_fill_left_cond, df=df_cond)
plt.fill_between(x_fill_left_cond, 0, y_fill_left_cond, color='salmon', alpha=0.6, label=f'Região de Rejeição (α/2={alpha_over_2_cond:.3f})')
x_fill_right_cond = np.linspace(t0_cond_right, 4, 100)
y_fill_right_cond = scipy.stats.t.pdf(x_fill_right_cond, df=df_cond)
plt.fill_between(x_fill_right_cond, 0, y_fill_right_cond, color='salmon', alpha=0.6)

plt.title(f'Teste de Hipótese para Condutividade (Bilateral, α = {alpha_cond:.2f})')
plt.xlabel('Estatística t')
plt.ylabel('Densidade de Probabilidade')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)
plt.show()

# e. Decida se rejeita a hipótese nula.
print(f"\ne. Decisão:")
if t_estatistica_cond < t0_cond_left or t_estatistica_cond > t0_cond_right:
    decisao_cond = "Rejeitar H₀"
else:
    decisao_cond = "Não rejeitar H₀"
print(f"   Decisão: {decisao_cond}")

# f. Interprete a decisão no contexto da afirmação original.
print(f"\nf. Interpretação da decisão:")
if decisao_cond == "Rejeitar H₀":
    print(f"   Há evidência estatística suficiente em α = {alpha_cond:.2f} para rejeitar a afirmação da indústria de que a condutividade média do rio é de {mu_0_cond} mg/l.")
else:
    print(f"   Não há evidência estatística suficiente em α = {alpha_cond:.2f} para rejeitar a afirmação da indústria de que a condutividade média do rio é de {mu_0_cond} mg/l.")