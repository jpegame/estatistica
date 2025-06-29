from scipy.stats import norm 

def mostra_area(z_score):
    area = norm.cdf(z_score)
    print(f'Área correspondente ao escore-z {z_score}: {area:.6f}')

#Exercicio a)
mostra_area(-2.19) #escore-z igual -2.19

#Exercicio b)
mostra_area(2.17) #escore-z igual 2.17
