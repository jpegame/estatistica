import numpy as np

n = 100
p = 0.34

# a. Identifique n, p e q.
q = 1 - p
print(f"a. Identificação:")
print(f"   n (número de tentativas) = {n}")
print(f"   p (probabilidade de sucesso) = {p}")
print(f"   q (probabilidade de fracasso) = {q:.2f}")

# b. Encontre os produtos np e nq.
np_produto = n * p
nq_produto = n * q
print(f"\nb. Produtos np e nq:")
print(f"   np = {np_produto}")
print(f"   nq = {nq_produto:.2f}")

# c. Determine se você pode usar uma distribuição normal para aproximar a distribuição de x.
pode_aproximar = (np_produto >= 5) and (nq_produto >= 5)
print(f"\nc. É possível usar uma distribuição normal para aproximar a distribuição de x? {'Sim' if pode_aproximar else 'Não'}")
if not pode_aproximar:
    print("   Não é possível porque as condições np >= 5 e/ou nq >= 5 não foram satisfeitas.")

# d. Calcule a média µ e o desvio padrão σ, se for apropriado.
if pode_aproximar:
    media_normal = np_produto
    desvio_padrao_normal = np.sqrt(n * p * q)
    print(f"\nd. Média (µ) da distribuição normal aproximada: {media_normal:.2f}")
    print(f"   Desvio Padrão (σ) da distribuição normal aproximada: {desvio_padrao_normal:.2f}")
else:
    print("\nd. Não é apropriado calcular a média e o desvio padrão para a aproximação normal, pois as condições não foram atendidas.")
     