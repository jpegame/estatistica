import numpy as np
import scipy.stats

n = 30 
x_barra = 22.9
sigma = 1.5
nivel_confianca = 0.90

# a. Identifique n, x-barra, σ e zc e encontre E.
zc = scipy.stats.norm.ppf(1 - (1 - nivel_confianca) / 2)

print(f"a. Identificação:")
print(f"   n (tamanho da amostra) = {n}")
print(f"   x̄ (média amostral) = {x_barra} anos")
print(f"   σ (desvio padrão da população) = {sigma} anos")
print(f"   z_c (valor crítico para {nivel_confianca*100:.0f}% de confiança) = {zc:.2f}")

# Calcule E (Margem de Erro)
E = zc * (sigma / np.sqrt(n))
print(f"   Margem de Erro (E) = {E:.2f} anos")

# b. Calcule os limites inferior e superior do intervalo de confiança.
limite_inferior = x_barra - E
limite_superior = x_barra + E

print(f"\nb. Intervalo de Confiança de {nivel_confianca*100:.0f}%:")
print(f"   Limite Inferior = {limite_inferior:.2f} anos")
print(f"   Limite Superior = {limite_superior:.2f} anos")
print(f"   O intervalo de confiança é: ({limite_inferior:.2f}, {limite_superior:.2f}) anos")

# c. Interprete os resultados.
print("\nc. Interpretação dos resultados:")
print(f"Estamos {nivel_confianca*100:.0f}% confiantes de que a verdadeira idade média de todos os estudantes atualmente matriculados na faculdade está entre {limite_inferior:.2f} e {limite_superior:.2f} anos.")
     