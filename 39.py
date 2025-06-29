# a. Formule as hipóteses nula e alternativa.
print("\na. Hipóteses Nula e Alternativa:")
print("   H₀: p ≤ 0.01 (A taxa de falha do paraquedas é de no máximo 1%)")
print("   Hₐ: p > 0.01 (A taxa de falha do paraquedas é maior que 1%)")

# b. Escreva os possíveis erros tipo I e II.
print("\nb. Possíveis Erros:")
print("   Erro Tipo I (α): Rejeitar H₀ quando H₀ é verdadeira.")
print("      Interpretação: Concluir que a taxa de falha é maior que 1% quando, na verdade, ela é ≤ 1%.")
print("      Consequência: A empresa é injustamente desacreditada e pode gastar recursos desnecessariamente.")
print("\n   Erro Tipo II (β): Não rejeitar H₀ quando H₀ é falsa.")
print("      Interpretação: Concluir que a taxa de falha é ≤ 1% quando, na verdade, ela é > 1%.")
print("      Consequência: Paraquedas com uma taxa de falha inaceitável são considerados seguros, colocando vidas em risco.")

# c. Indique qual erro é mais sério.
print("\nc. Qual erro é mais sério?")
print("   Neste contexto, o **Erro Tipo II é mais grave**.")
print("   Um Erro Tipo II significa que paraquedas perigosos (com taxa de falha > 1%) seriam considerados seguros, o que poderia resultar em acidentes graves ou fatais para os usuários.")
print("As consequências de um Erro Tipo II (risco de vida) superam as consequências de um Erro Tipo I (prejuízo de reputação e financeiro para a empresa).")