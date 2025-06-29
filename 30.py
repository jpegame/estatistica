import numpy as np
import scipy.stats

n = 36 
x_barra = 9.75
s = 2.39

niveis_confianca = [0.90, 0.95] # Níveis de confiança a serem calculados

# Graus de liberdade
df = n - 1
print(f"Graus de liberdade (df) = n - 1 = {df}")

margens_erro = {}
intervalos = {}

for nivel_confianca in niveis_confianca:
    print(f"\n--- Intervalo de Confiança de {nivel_confianca*100:.0f}% ---")

    # a. Encontre tc e calcule E para cada nível de confiança.
    alpha_over_2 = (1 - nivel_confianca) / 2
    tc = scipy.stats.t.ppf(1 - alpha_over_2, df=df)

    print(f"a. t_c (valor crítico para {nivel_confianca*100:.0f}% de confiança, df={df}) = {tc:.3f}")

    E = tc * (s / np.sqrt(n))
    margens_erro[nivel_confianca] = E
    print(f"   Margem de Erro (E) = {E:.2f} dias")

    # b. Use x-barra e E para encontrar os limites inferior e superior.
    limite_inferior = x_barra - E
    limite_superior = x_barra + E
    intervalos[nivel_confianca] = (limite_inferior, limite_superior)

    print(f"b. Intervalo de Confiança: ({limite_inferior:.2f}, {limite_superior:.2f}) dias")

# c. Interprete os resultados e compare as larguras dos intervalos de confiança.
print("\nc. Interpretação dos resultados e comparação das larguras:")

for nivel_confianca, (inf, sup) in intervalos.items():
    largura = sup - inf
    print(f"Para {nivel_confianca*100:.0f}% de confiança, estamos confiantes de que a verdadeira média populacional está entre {inf:.2f} e {sup:.2f} dias. Largura: {largura:.2f} dias.")

print("\nComparação:")
largura_90 = intervalos[0.90][1] - intervalos[0.90][0]
largura_95 = intervalos[0.95][1] - intervalos[0.95][0]

print(f"A largura do intervalo de 90% é {largura_90:.2f} dias.")
print(f"A largura do intervalo de 95% é {largura_95:.2f} dias.")
print("Como esperado, o intervalo de confiança de 95% é mais largo do que o intervalo de 90%.")
print("Isso ocorre porque, para ter uma confiança maior de que o intervalo captura a verdadeira média populacional, precisamos de um intervalo mais amplo.")
     