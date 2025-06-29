import scipy.stats

tamanho_amostra = 22
nivel_confianca = 0.90

# a. Identifique os graus de liberdade.
graus_liberdade = tamanho_amostra - 1
print(f"a. Graus de liberdade (df) = n - 1 = {tamanho_amostra} - 1 = {graus_liberdade}")

# b. Identifique o nível de confiança c.
print(f"b. Nível de confiança (c) = {nivel_confianca*100:.0f}%")

# c. Use a Tabela para encontrar tc.
tc = scipy.stats.t.ppf(1 - (1 - nivel_confianca) / 2, df=graus_liberdade)
print(f"\nc. O valor crítico t_c para df={graus_liberdade} e confiança de {nivel_confianca*100:.0f}% é: {tc:.3f}")

# d. Interprete os resultados.
print("\nd. Interpretação dos resultados:")
print(f"O valor crítico t_c de {tc:.3f} significa que, em uma distribuição t de Student com {graus_liberdade} graus de liberdade, {90}% da área está entre -{tc:.3f} e +{tc:.3f}.")
print("Este valor é usado para construir intervalos de confiança ou realizar testes de hipóteses quando o desvio padrão populacional é desconhecido e o tamanho da amostra é pequeno (ou quando a distribuição t é mais apropriada).")
     