import numpy as np

horas_trabalhadas = [
    26, 25, 32, 31, 28, 28,
    28, 22, 28, 25, 21, 40,
    32, 22, 25, 22, 26, 24,
    46, 20, 35, 22, 32, 48,
    32, 36, 38, 32, 22, 19
]

# a. Encontre a média amostral.
# Usando numpy.mean() para calcular a média
media_amostral = np.mean(horas_trabalhadas)

print(f"a. A média amostral (x̄) do número de horas semanais trabalhadas é: {media_amostral:.2f} horas")

# b. Estime a média populacional.
# A média amostral é a melhor estimativa pontual para a média populacional.
estimativa_media_populacional = media_amostral

print(f"\nb. A estimativa pontual para a média populacional (µ) é a média amostral:")
print(f"   Estimativa de µ = {estimativa_media_populacional:.2f} horas")

print("\nInterpretação:")
print(f"Com base na amostra de 30 funcionários, estimamos que a média de horas semanais trabalhadas por funcionários de mercearias no condado seja de aproximadamente {estimativa_media_populacional:.2f} horas.")
     