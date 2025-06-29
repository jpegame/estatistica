import numpy as np
import scipy.stats

# Dados da amostra do Exercício 24
horas_trabalhadas_amostra = [
    26, 25, 32, 31, 28, 28,
    28, 22, 28, 25, 21, 40,
    32, 22, 25, 22, 26, 24,
    46, 20, 35, 22, 32, 48,
    32, 36, 38, 32, 22, 19
]
n = len(horas_trabalhadas_amostra)
media_amostral = np.mean(horas_trabalhadas_amostra) # x_barra

# Dados fornecidos para a Questão 25
desvio_padrao_populacao = 7.9 # σ
nivel_confianca = 0.95

# a. Identifique zc, n e σ.
# Para um nível de confiança de 95%, a área nas duas caudas é 1 - 0.95 = 0.05.
# A área em cada cauda é 0.05 / 2 = 0.025.
# O valor zc corresponde à área acumulada de 1 - 0.025 = 0.975.
zc = scipy.stats.norm.ppf(1 - (1 - nivel_confianca) / 2)

print(f"a. Identificação:")
print(f"   z_c (valor crítico para {nivel_confianca*100:.0f}% de confiança) = {zc:.2f}")
print(f"   n (tamanho da amostra) = {n}")
print(f"   σ (desvio padrão da população) = {desvio_padrao_populacao} horas")

# b. Calcule E usando zc, σ e n.
E = zc * (desvio_padrao_populacao / np.sqrt(n))
print(f"\nb. Margem de Erro (E) = {E:.2f} horas")

# c. Interprete os resultados da Questão 25.
print("\nc. Interpretação dos resultados da Questão 25:")
print(f"A margem de erro para o número médio de horas trabalhadas por funcionários de mercearias é de {E:.2f} horas.")
print("Isso significa que a média da amostra (29.70 horas) pode variar em até 2.83 horas para cima ou para baixo para abranger a verdadeira média populacional com 95% de confiança.")

print("\n" + "="*30 + "\n") # Separador para a próxima questão

print("--- Questão 26 ---")

# a. Calcule x-barra e E. (Já calculados acima)
print(f"a. Média amostral (x̄) = {media_amostral:.2f} horas (do Exercício 24)")
print(f"   Margem de Erro (E) = {E:.2f} horas (da Questão 25)")

# b. Calcule os limites inferior e superior do intervalo de confiança.
limite_inferior = media_amostral - E
limite_superior = media_amostral + E

print(f"\nb. Intervalo de Confiança de {nivel_confianca*100:.0f}%:")
print(f"   Limite Inferior = {limite_inferior:.2f} horas")
print(f"   Limite Superior = {limite_superior:.2f} horas")
print(f"   O intervalo de confiança é: ({limite_inferior:.2f}, {limite_superior:.2f}) horas")

# c. Interprete os resultados da Questão 26.
print("\nc. Interpretação dos resultados da Questão 26:")
print(f"Estamos 95% confiantes de que o número médio real de horas semanais trabalhadas por todos os funcionários de mercearias no condado está entre {limite_inferior:.2f} e {limite_superior:.2f} horas.")