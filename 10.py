import scipy.stats

print("--- Questão 10.1 ---")

area_direita = 0.9616
area_esquerda = 1 - area_direita

z_score = scipy.stats.norm.ppf(area_esquerda)

print(f"A área à direita é de {area_direita*100:.2f}%.")
print(f"A área à esquerda (acumulada) é de {area_esquerda*100:.2f}%.")
print(f"O escore-z que corresponde a ter 96,16% da área à sua direita é: {z_score:.2f}")

print("\n--- Questão 10.2 ---")

area_central = 0.95
area_nas_caudas = 1 - area_central
area_uma_cauda = area_nas_caudas / 2

# a. Determine a área acumulada.
area_acumulada_z_negativo = area_uma_cauda
area_acumulada_z_positivo = area_central + area_uma_cauda

print(f"a. A área acumulada à esquerda de -z é: {area_acumulada_z_negativo:.4f}")
print(f"   A área acumulada à esquerda de +z é: {area_acumulada_z_positivo:.4f}")

# b. Localize a área na tabela normal padrão. (Feito pela função ppf)
# c. Encontre o escore-z que corresponde à área.
z_negativo = scipy.stats.norm.ppf(area_acumulada_z_negativo)
z_positivo = scipy.stats.norm.ppf(area_acumulada_z_positivo)

print(f"c. O escore-z negativo é: {z_negativo:.2f}")
print(f"   O escore-z positivo é: {z_positivo:.2f}")
print(f"Portanto, o escore-z para o qual 95% da área de distribuição esteja entre -z e z é aproximadamente +/- {z_positivo:.2f}.")