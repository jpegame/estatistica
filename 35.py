import numpy as np
import scipy.stats

margem_erro_q35 = 0.02 # E = 2%
nivel_confianca_q35 = 0.90

# zc para 90% de confiança
zc_q35 = scipy.stats.norm.ppf(1 - (1 - nivel_confianca_q35) / 2)

print(f"a. Identificação dos parâmetros comuns:")
print(f"   Margem de Erro (E) = {margem_erro_q35*100:.0f}%")
print(f"   z_c (valor crítico para {nivel_confianca_q35*100:.0f}% de confiança) = {zc_q35:.2f}")

# Cenário 1: Não há estimativa preliminar disponível
print("\n--- Cenário 1: Sem estimativa preliminar de p-chapéu ---")
p_chapeu_cenario1 = 0.5 # Usamos 0.5 para maximizar o tamanho da amostra
q_chapeu_cenario1 = 1 - p_chapeu_cenario1

print(f"a. p-chapéu = {p_chapeu_cenario1:.1f}, q-chapéu = {q_chapeu_cenario1:.1f}")

# b. Calcule o tamanho mínimo da amostra n.
n_cenario1_calculado = (p_chapeu_cenario1 * q_chapeu_cenario1) * (zc_q35 / margem_erro_q35)**2
n_cenario1 = np.ceil(n_cenario1_calculado) # Arredondar para cima

print(f"b. Tamanho mínimo da amostra calculado (n) = {n_cenario1_calculado:.2f}")
print(f"c. Quantos adultos devem ser incluídos na amostra (arredondado para cima) = {int(n_cenario1)}")

# Cenário 2: Uma pesquisa anterior descobriu que 31%
print("\n--- Cenário 2: Com estimativa preliminar de p-chapéu = 0.31 ---")
p_chapeu_cenario2 = 0.31
q_chapeu_cenario2 = 1 - p_chapeu_cenario2

print(f"a. p-chapéu = {p_chapeu_cenario2:.2f}, q-chapéu = {q_chapeu_cenario2:.2f}")

# b. Calcule o tamanho mínimo da amostra n.
n_cenario2_calculado = (p_chapeu_cenario2 * q_chapeu_cenario2) * (zc_q35 / margem_erro_q35)**2
n_cenario2 = np.ceil(n_cenario2_calculado) # Arredondar para cima

print(f"b. Tamanho mínimo da amostra calculado (n) = {n_cenario2_calculado:.2f}")
print(f"c. Quantos adultos devem ser incluídos na amostra (arredondado para cima) = {int(n_cenario2)}")

print("\nInterpretação:")
print(f"No cenário 1 (sem estimativa preliminar), são necessários {int(n_cenario1)} adultos para a amostra.")
print(f"No cenário 2 (com estimativa preliminar de 31%), são necessários {int(n_cenario2)} adultos para a amostra.")
print("É necessário um tamanho de amostra maior quando não há estimativa preliminar, pois o valor de p-chapéu = 0.5 maximiza o produto p-chapéu * q-chapéu, garantindo que o tamanho da amostra seja grande o suficiente para qualquer proporção verdadeira.")
     