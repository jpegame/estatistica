import numpy as np
import scipy.stats

n = 498
proporcao_amostral = 0.25
nivel_confianca = 0.99

# a. Encontre p-chapéu e q-chapéu.
p_chapeu = proporcao_amostral
q_chapeu = 1 - p_chapeu
print(f"a. p-chapéu (proporção amostral) = {p_chapeu:.2f}")
print(f"   q-chapéu = {q_chapeu:.2f}")

# b. Verifique se a distribuição amostral de p-chapéu pode ser aproximada por uma distribuição normal.
np_chapeu = n * p_chapeu
nq_chapeu = n * q_chapeu
pode_aproximar_normal = (np_chapeu >= 5) and (nq_chapeu >= 5)

print(f"\nb. Verificação da aproximação normal:")
print(f"   n * p-chapéu = {np_chapeu:.2f}")
print(f"   n * q-chapéu = {nq_chapeu:.2f}")
print(f"   É possível aproximar por uma distribuição normal? {'Sim' if pode_aproximar_normal else 'Não'}")

if not pode_aproximar_normal:
    print("   (Não é possível construir o intervalo de confiança usando a aproximação normal.)")
    # Para fins de demonstração, o código prosseguirá, mas em um cenário real, você pararia aqui.

# c. Encontre zc e E.
zc = scipy.stats.norm.ppf(1 - (1 - nivel_confianca) / 2)
print(f"\nc. z_c (valor crítico para {nivel_confianca*100:.0f}% de confiança) = {zc:.2f}")

# Calcule E (Margem de Erro) para proporções
E = zc * np.sqrt((p_chapeu * q_chapeu) / n)
print(f"   Margem de Erro (E) = {E:.4f}")

# d. Use p-chapéu e E para calcular os limites inferior e superior do intervalo de confiança.
limite_inferior = p_chapeu - E
limite_superior = p_chapeu + E

print(f"\nd. Intervalo de Confiança de {nivel_confianca*100:.0f}%:")
print(f"   Limite Inferior = {limite_inferior:.4f}")
print(f"   Limite Superior = {limite_superior:.4f}")
print(f"   O intervalo de confiança é: ({limite_inferior:.4f}, {limite_superior:.4f})")

# e. Interprete os resultados.
print("\ne. Interpretação dos resultados:")
print(f"Estamos {nivel_confianca*100:.0f}% confiantes de que a verdadeira proporção populacional de adultos que consideram pessoas acima de 65 anos como os motoristas mais perigosos está entre {limite_inferior*100:.2f}% e {limite_superior*100:.2f}%.")
     