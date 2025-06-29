n_q31 = 18
s_q31 = 2.5
populacao_normal = True

print("Deveremos usar a distribuição normal padrão, a distribuição t ou nenhuma delas para construir um intervalo de confiança de 90% para a média da frequência cardíaca populacional?")
print("\nExplicação do Raciocínio:")

print("1. Desvio Padrão Populacional (σ): O desvio padrão da população não é conhecido. Foi fornecido apenas o desvio padrão AMOSTRAL (s = 2.5 batimentos por minuto).")
print(f"2. Tamanho da Amostra (n): O tamanho da amostra é {n_q31}, que é PEQUENO (menor que 30).")
print("3. Distribuição da População: O problema afirma que as frequências cardíacas são NORMALMENTE DISTRIBUÍDAS.")

print("\nRegras para Intervalos de Confiança para a Média:")
print(" - Se σ é conhecido: Usar a Distribuição Normal Padrão (Z-score).")
print(" - Se σ é desconhecido e n >= 30: Usar a Distribuição Normal Padrão (Z-score), usando s como estimativa de σ (pelo Teorema do Limite Central).")
print(" - Se σ é desconhecido e n < 30: Usar a Distribuição t de Student, DESDE QUE a população seja normalmente distribuída ou a amostra seja grande o suficiente para o Teorema do Limite Central (o que não é o caso aqui).")
print(" - Se σ é desconhecido e n < 30 e a população NÃO é normalmente distribuída: Não é possível usar métodos paramétricos (Z ou t) de forma confiável.")

print(f"\nConclusão para este problema:")
print(f"Como o desvio padrão da população (σ) é DESCONHECIDO, o tamanho da amostra (n = {n_q31}) é PEQUENO, e a população é NORMALMENTE DISTRIBUÍDA, a distribuição apropriada para construir o intervalo de confiança é a **DISTRIBUIÇÃO t de Student**.")