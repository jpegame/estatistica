import scipy.stats

percentis = {
    "P10º": 0.10,
    "P20º": 0.20,
    "P99º": 0.99
}

for percentil, area_esquerda in percentis.items():
    print(f"\n{percentil}:")
    print(f"a. A área acumulada para o {percentil} é: {area_esquerda:.4f}")
    z_score = scipy.stats.norm.ppf(area_esquerda)
    print(f"c. O escore-z que corresponde ao {percentil} é: {z_score:.2f}")