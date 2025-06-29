import numpy as np
import scipy.stats

n = 30
s = 1.20
s_quadrado = s**2

niveis_confianca = [0.90, 0.95] # Níveis de confiança a serem calculados

# Graus de liberdade
df = n - 1
print(f"Graus de liberdade (df) = n - 1 = {df}")
print(f"Variância amostral (s²) = {s_quadrado:.2f} (miligramas²)")

for nivel_confianca in niveis_confianca:
    print(f"\n--- Intervalo de Confiança de {nivel_confianca*100:.0f}% ---")

    # a. Encontre os valores críticos de χ²R e χ²L para cada intervalo de confiança.
    # Área nas caudas = (1 - nível_confianca). Cada cauda tem metade disso.
    alpha_over_2 = (1 - nivel_confianca) / 2

    chi2_L = scipy.stats.chi2.ppf(alpha_over_2, df=df)
    chi2_R = scipy.stats.chi2.ppf(1 - alpha_over_2, df=df)

    print(f"a. Valores críticos Qui-Quadrado para df={df}:")
    print(f"   χ²_L (cauda esquerda, área à esquerda={alpha_over_2:.3f}) = {chi2_L:.3f}")
    print(f"   χ²_R (cauda direita, área à esquerda={1-alpha_over_2:.3f}) = {chi2_R:.3f}")

    # b. Calcule os limites inferior e superior para a variância populacional.
    limite_inferior_variancia = ((n - 1) * s_quadrado) / chi2_R
    limite_superior_variancia = ((n - 1) * s_quadrado) / chi2_L

    print(f"\nb. Intervalo de Confiança para a VARIÂNCIA Populacional (σ²):")
    print(f"   Limite Inferior = {limite_inferior_variancia:.3f} miligramas²")
    print(f"   Limite Superior = {limite_superior_variancia:.3f} miligramas²")

    # c. Calcule as raízes quadradas dos limites para o desvio padrão.
    limite_inferior_desvio_padrao = np.sqrt(limite_inferior_variancia)
    limite_superior_desvio_padrao = np.sqrt(limite_superior_variancia)

    # d. Especifique os intervalos de confiança.
    print(f"\nd. Intervalo de Confiança de {nivel_confianca*100:.0f}% para a VARIÂNCIA Populacional (σ²):")
    print(f"   ({limite_inferior_variancia:.3f}, {limite_superior_variancia:.3f}) miligramas²")

    print(f"   Intervalo de Confiança de {nivel_confianca*100:.0f}% para o DESVIO PADRÃO Populacional (σ):")
    print(f"   ({limite_inferior_desvio_padrao:.3f}, {limite_superior_desvio_padrao:.3f}) miligramas")

    print(f"\nInterpretação para {nivel_confianca*100:.0f}% de confiança:")
    print(f"Estamos {nivel_confianca*100:.0f}% confiantes de que a verdadeira variância populacional dos pesos dos remédios está entre {limite_inferior_variancia:.3f} e {limite_superior_variancia:.3f} miligramas².")
    print(f"E estamos {nivel_confianca*100:.0f}% confiantes de que o verdadeiro desvio padrão populacional está entre {limite_inferior_desvio_padrao:.3f} e {limite_superior_desvio_padrao:.3f} miligramas.")