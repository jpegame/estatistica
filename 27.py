import numpy as np
import scipy.stats

margem_erro = 2.0
nivel_confianca = 0.95
desvio_padrao_populacao = 7.9

# 1. Encontre zc para o nível de confiança de 95%.
zc = scipy.stats.norm.ppf(1 - (1 - nivel_confianca) / 2)

print(f"z_c (valor crítico para {nivel_confianca*100:.0f}% de confiança) = {zc:.2f}")
print(f"σ (desvio padrão da população) = {desvio_padrao_populacao} horas")
print(f"E (margem de erro máxima) = {margem_erro} horas")

# 2. Calcule n usando a fórmula.
tamanho_amostra_calculado = ((zc * desvio_padrao_populacao) / margem_erro)**2

# O tamanho da amostra deve ser um número inteiro, e sempre arredondamos para cima.
n_necessario = np.ceil(tamanho_amostra_calculado)

print(f"\nO tamanho da amostra calculado (n) é: {tamanho_amostra_calculado:.2f}")
print(f"Portanto, o número de funcionários que devem ser incluídos na amostra é: {int(n_necessario)}")

print("\nInterpretação:")
print(f"Para estar 95% confiante de que a média amostral não difere da média populacional em mais de 2.0 horas, o pesquisador deve incluir pelo menos {int(n_necessario)} funcionários na amostra.")