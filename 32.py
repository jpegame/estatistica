n_q32 = 2462
x_q32 = 123

# a. Identifique x e n.
print(f"a. Identificação:")
print(f"   x (número de sucessos) = {x_q32}")
print(f"   n (tamanho da amostra) = {n_q32}")

# b. Use x e n para encontrar p-chapéu.
p_chapeu = x_q32 / n_q32
print(f"\nb. p-chapéu (proporção amostral) = {p_chapeu:.4f}")

print("\nInterpretação:")
print(f"A proporção amostral de professores que consideram as informações de busca confiáveis é de aproximadamente {p_chapeu*100:.2f}%.")
     