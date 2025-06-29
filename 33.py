import numpy as np
import scipy.stats

n_q33 = 2462
x_q33 = 123
nivel_confianca_q33 = 0.90

# a. Encontre p-chapéu e q-chapéu.
p_chapeu = x_q33 / n_q33
q_chapeu = 1 - p_chapeu
print(f"a. p-chapéu (proporção amostral) = {p_chapeu:.4f}")
print(f"   q-chapéu = {q_chapeu:.4f}")

# b. Verifique se a distribuição amostral de p-chapéu pode ser aproximada por uma distribuição normal.
np_chapeu = n_q33 * p_chapeu
nq_chapeu = n_q33 * q_chapeu
pode_aproximar_normal = (np_chapeu >= 5) and (nq_chapeu >= 5)

print(f"\nb. Verificação da aproximação normal:")
print(f"   n * p-chapéu = {np_chapeu:.2f}")
print(f"   n * q-chapéu = {nq_chapeu:.2f}")
print(f"   É possível aproximar por uma distribuição normal? {'Sim' if pode_aproximar_normal else 'Não'}")

if not pode_aproximar_normal:
    print("   (Não é possível construir o intervalo de confiança usando a aproximação normal.)")
    exit() # Interrompe a execução se a aproximação não for válida

# c. Encontre zc e E.
# zc para 90% de confiança
zc_q33 = scipy.stats.norm.ppf(1 - (1 - nivel_confianca_q33) / 2)
print(f"\nc. z_c (valor crítico para {nivel_confianca_q33*100:.0f}% de confiança) = {zc_q33:.2f}")

# Calcule E (Margem de Erro) para proporções
E_q33 = zc_q33 * np.sqrt((p_chapeu * q_chapeu) / n_q33)
print(f"   Margem de Erro (E) = {E_q33:.4f}")

# d. Use p-chapéu e E para calcular os limites inferior e superior do intervalo de confiança.
limite_inferior_q33 = p_chapeu - E_q33
limite_superior_q33 = p_chapeu + E_q33

print(f"\nd. Intervalo de Confiança de {nivel_confianca_q33*100:.0f}%:")
print(f"   Limite Inferior = {limite_inferior_q33:.4f}")
print(f"   Limite Superior = {limite_superior_q33:.4f}")
print(f"   O intervalo de confiança é: ({limite_inferior_q33:.4f}, {limite_superior_q33:.4f})")

# e. Interprete os resultados.
print("\ne. Interpretação dos resultados:")
print(f"Estamos {nivel_confianca_q33*100:.0f}% confiantes de que a verdadeira proporção populacional de professores americanos que consideram as informações de busca on-line corretas/confiáveis está entre {limite_inferior_q33*100:.2f}% e {limite_superior_q33*100:.2f}%.")
     