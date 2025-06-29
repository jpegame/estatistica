import numpy as np
import scipy.stats

n = 16
x_barra = 162.0
s = 10.0

niveis_confianca = [0.90, 0.99] # Níveis de confiança a serem calculados

# Graus de liberdade
df = n - 1
print(f"Graus de liberdade (df) = n - 1 = {df}")

for nivel_confianca in niveis_confianca:
    print(f"\n--- Intervalo de Confiança de {nivel_confianca*100:.0f}% ---")

    # Encontrar t_c (valor crítico de t)
    # A área em cada cauda é (1 - nível_confianca) / 2
    alpha_over_2 = (1 - nivel_confianca) / 2
    tc = scipy.stats.t.ppf(1 - alpha_over_2, df=df)

    print(f"t_c (valor crítico para {nivel_confianca*100:.0f}% de confiança, df={df}) = {tc:.3f}")

    # Calcular a Margem de Erro (E)
    E = tc * (s / np.sqrt(n))
    print(f"Margem de Erro (E) = {E:.2f} ºF")

    # Calcular os limites do Intervalo de Confiança
    limite_inferior = x_barra - E
    limite_superior = x_barra + E

    print(f"Intervalo de Confiança: ({limite_inferior:.2f}, {limite_superior:.2f}) ºF")

    # Interpretação
    print(f"Estamos {nivel_confianca*100:.0f}% confiantes de que a verdadeira temperatura média da população de cafés vendidos está entre {limite_inferior:.2f} ºF e {limite_superior:.2f} ºF.")
     