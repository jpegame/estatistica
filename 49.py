import scipy.stats
import matplotlib.pyplot as plt
import numpy as np

mu_0_salario = 68000
n_salario = 20 
x_barra_salario = 66900
sigma_salario = 5500
alpha_salario = 0.05

# a. Formulação das hipóteses
print("a. Formulação das Hipóteses:")
print(f"   H₀: μ ≥ {mu_0_salario} (Salário médio é maior ou igual a US$ {mu_0_salario})")
print(f"   Hₐ: μ < {mu_0_salario} (Salário médio é menor que US$ {mu_0_salario} - AFIRMAÇÃO DOS FUNCIONÁRIOS)")
print("   Tipo de Teste: Unilateral à esquerda")

# b. Nível de significância
print(f"\nb. Nível de Significância (α) = {alpha_salario:.2f}")

# c. Encontre o valor crítico zc.
# Para um teste unilateral à esquerda, zc é o valor que deixa α de área à sua esquerda.
zc_salario = scipy.stats.norm.ppf(alpha_salario)
print(f"\nc. Valor crítico z_c = {zc_salario:.2f}")

# d. Calcule a estatística de teste padronizada z.
erro_padrao_salario = sigma_salario / np.sqrt(n_salario)
z_estatistica_salario = (x_barra_salario - mu_0_salario) / erro_padrao_salario
print(f"   Estatística de teste z = {z_estatistica_salario:.2f}")

# e. Decisão
print("\ne. Decisão (abordagem do valor crítico):")
if z_estatistica_salario < zc_salario:
    decisao_salario = "Rejeitar H₀"
    interpretacao_salario = f"Há evidência estatística suficiente em α = {alpha_salario:.2f} para apoiar a afirmação dos funcionários de que o salário médio dos engenheiros mecânicos é menor que US$ {mu_0_salario}."
else:
    decisao_salario = "Não rejeitar H₀"
    interpretacao_salario = f"Não há evidência estatística suficiente em α = {alpha_salario:.2f} para apoiar a afirmação dos funcionários de que o salário médio dos engenheiros mecânicos é menor que US$ {mu_0_salario}."

print(f"   Decisão: {decisao_salario}")
print(f"   Interpretação: {interpretacao_salario}")

# Gráfico para o Teste 1 (Salário)
x_vals_salario = np.linspace(mu_0_salario - 3 * erro_padrao_salario, mu_0_salario + 3 * erro_padrao_salario, 500)
y_vals_salario = scipy.stats.norm.pdf(x_vals_salario, loc=mu_0_salario, scale=erro_padrao_salario)

plt.figure(figsize=(10, 6))
plt.plot(x_vals_salario, y_vals_salario, color='blue', label='Distribuição Amostral de Salários')
plt.axvline(mu_0_salario, color='gray', linestyle='--', linewidth=0.8, label=f'Média H₀ = ${mu_0_salario}')
plt.axvline(zc_salario * erro_padrao_salario + mu_0_salario, color='red', linestyle='--', label=f'Limite Crítico z_c = {zc_salario:.2f}')
plt.axvline(x_barra_salario, color='green', linestyle='-', label=f'Média Amostral = ${x_barra_salario}')

x_rejeicao_salario = np.linspace(x_vals_salario.min(), zc_salario * erro_padrao_salario + mu_0_salario, 100)
y_rejeicao_salario = scipy.stats.norm.pdf(x_rejeicao_salario, loc=mu_0_salario, scale=erro_padrao_salario)
plt.fill_between(x_rejeicao_salario, 0, y_rejeicao_salario, color='salmon', alpha=0.6, label=f'Região de Rejeição (α={alpha_salario})')

plt.title('Teste de Hipótese para Salário de Engenheiros (Unilateral à Esquerda)')
plt.xlabel('Salário (US$)')
plt.ylabel('Densidade de Probabilidade')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)
plt.ticklabel_format(style='plain', axis='x')
plt.show()


# --- Teste 2: Dia de Trabalho dos Engenheiros Mecânicos ---
print("\n" + "="*60 + "\n") # Separador
print("--- Questão 49 - Teste 2: Dia de Trabalho dos Engenheiros Mecânicos ---")

# Dados fornecidos
mu_0_horas = 8.5    # horas (Média hipotética da H0)
n_horas = 25        # Tamanho da amostra
x_barra_horas = 8.2 # horas (Média amostral)
sigma_horas = 0.5   # horas (Desvio padrão populacional)
alpha_horas = 0.01  # Nível de significância

# a. Formulação das hipóteses
print("a. Formulação das Hipóteses:")
print(f"   H₀: μ ≥ {mu_0_horas} (Dia de trabalho médio é maior ou igual a {mu_0_horas} horas)")
print(f"   Hₐ: μ < {mu_0_horas} (Dia de trabalho médio é menor que {mu_0_horas} horas - AFIRMAÇÃO DO PRESIDENTE)")
print("   Tipo de Teste: Unilateral à esquerda")

# b. Nível de significância
print(f"\nb. Nível de Significância (α) = {alpha_horas:.2f}")

# c. Encontre o valor crítico zc.
zc_horas = scipy.stats.norm.ppf(alpha_horas)
print(f"\nc. Valor crítico z_c = {zc_horas:.2f}")

# d. Calcule a estatística de teste padronizada z.
erro_padrao_horas = sigma_horas / np.sqrt(n_horas)
z_estatistica_horas = (x_barra_horas - mu_0_horas) / erro_padrao_horas
print(f"   Estatística de teste z = {z_estatistica_horas:.2f}")

# e. Decisão
print("\ne. Decisão (abordagem do valor crítico):")
if z_estatistica_horas < zc_horas:
    decisao_horas = "Rejeitar H₀"
    interpretacao_horas = f"Há evidência estatística suficiente em α = {alpha_horas:.2f} para apoiar a afirmação do presidente de que o dia de trabalho médio dos engenheiros mecânicos é menor que {mu_0_horas} horas."
else:
    decisao_horas = "Não rejeitar H₀"
    interpretacao_horas = f"Não há evidência estatística suficiente em α = {alpha_horas:.2f} para apoiar a afirmação do presidente de que o dia de trabalho médio dos engenheiros mecânicos é menor que {mu_0_horas} horas."

print(f"   Decisão: {decisao_horas}")
print(f"   Interpretação: {interpretacao_horas}")

# Gráfico para o Teste 2 (Dia de Trabalho)
x_vals_horas = np.linspace(mu_0_horas - 3 * erro_padrao_horas, mu_0_horas + 3 * erro_padrao_horas, 500)
y_vals_horas = scipy.stats.norm.pdf(x_vals_horas, loc=mu_0_horas, scale=erro_padrao_horas)

plt.figure(figsize=(10, 6))
plt.plot(x_vals_horas, y_vals_horas, color='blue', label='Distribuição Amostral de Horas Trabalhadas')
plt.axvline(mu_0_horas, color='gray', linestyle='--', linewidth=0.8, label=f'Média H₀ = {mu_0_horas} horas')
plt.axvline(zc_horas * erro_padrao_horas + mu_0_horas, color='red', linestyle='--', label=f'Limite Crítico z_c = {zc_horas:.2f}')
plt.axvline(x_barra_horas, color='green', linestyle='-', label=f'Média Amostral = {x_barra_horas} horas')

x_rejeicao_horas = np.linspace(x_vals_horas.min(), zc_horas * erro_padrao_horas + mu_0_horas, 100)
y_rejeicao_horas = scipy.stats.norm.pdf(x_rejeicao_horas, loc=mu_0_horas, scale=erro_padrao_horas)
plt.fill_between(x_rejeicao_horas, 0, y_rejeicao_horas, color='salmon', alpha=0.6, label=f'Região de Rejeição (α={alpha_horas})')

plt.title('Teste de Hipótese para Dia de Trabalho (Unilateral à Esquerda)')
plt.xlabel('Horas de Trabalho')
plt.ylabel('Densidade de Probabilidade')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)
plt.show()