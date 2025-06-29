import scipy.stats

n_q36 = 30
nivel_confianca_q36 = 0.90

# a. Identifique os graus de liberdade e o nível de confiança.
graus_liberdade_q36 = n_q36 - 1
print(f"a. Graus de liberdade (df) = n - 1 = {graus_liberdade_q36}")
print(f"   Nível de confiança (c) = {nivel_confianca_q36*100:.0f}%")

# b. Encontre as áreas à direita de χ²R e χ²L.
area_cauda_esquerda = 0.05
area_cauda_direita = 0.05

print(f"\nb. Áreas à direita:")
print(f"   Área à direita de χ²_R (cauda superior) = {area_cauda_direita:.2f}")
print(f"   Área à direita de χ²_L (cauda inferior) = {1 - area_cauda_esquerda:.2f} (ou seja, 0.95)")

# c. Use a Tabela para encontrar χ²_R e χ²_L.
chi2_L = scipy.stats.chi2.ppf(area_cauda_esquerda, df=graus_liberdade_q36)
chi2_R = scipy.stats.chi2.ppf(1 - area_cauda_direita, df=graus_liberdade_q36)

print(f"\nc. Valores críticos Qui-Quadrado:")
print(f"   χ²_L (valor crítico esquerdo) = {chi2_L:.3f}")
print(f"   χ²_R (valor crítico direito) = {chi2_R:.3f}")

# d. Interprete os resultados.
print("\nd. Interpretação dos resultados:")
print(f"Para uma distribuição Qui-Quadrado com {graus_liberdade_q36} graus de liberdade, {90}% da área está entre {chi2_L:.3f} e {chi2_R:.3f}.")
print("Esses valores são usados para construir intervalos de confiança para a variância ou desvio padrão populacional.")
     