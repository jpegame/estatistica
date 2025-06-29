media_peso = 52      # libras (m)
desvio_padrao_peso = 15 # libras (s)

print(f"a. Média (μ) = {media_peso} libras, Desvio Padrão (σ) = {desvio_padrao_peso} libras.")

escores_z_dados = [-2.33, 3.10, 0.58]
pesos_calculados = []

print("\nb. Transforme cada escore-z em um valor x:")
for z in escores_z_dados:
    x_peso = media_peso + z * desvio_padrao_peso
    pesos_calculados.append((z, x_peso))
    print(f"Para z = {z}, o peso x é: {x_peso:.2f} libras")

print("\nc. Interprete os resultados:")
for z, x_peso in pesos_calculados:
    if z < 0:
        print(f"Um cão com z = {z} tem um peso de {x_peso:.2f} libras, o que está {abs(z):.2f} desvios padrão ABAIXO da média.")
    elif z > 0:
        print(f"Um cão com z = {z} tem um peso de {x_peso:.2f} libras, o que está {z:.2f} desvios padrão ACIMA da média.")
    else:
        print(f"Um cão com z = {z} tem um peso de {x_peso:.2f} libras, o que é EXATAMENTE a média.")

print("\nInterpretação geral:")
print("Cães com z-scores negativos têm pesos abaixo da média, enquanto cães com z-scores positivos têm pesos acima da média. Quanto maior o valor absoluto do z-score, mais distante da média o peso está.")
print("Por exemplo, um cão com z = -2.33 (2.33 desvios padrão abaixo da média) pesa 17.05 libras, sendo consideravelmente mais leve que a média.")
print("Um cão com z = 3.10 (3.10 desvios padrão acima da média) pesa 98.50 libras, sendo consideravelmente mais pesado que a média.")
print("Um cão com z = 0.58 (0.58 desvios padrão acima da média) pesa 60.70 libras, sendo um pouco mais pesado que a média.")