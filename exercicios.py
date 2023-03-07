#Exercício de Soma
"""n1 = int(input("Digite um número:"))
n2 = int(input("Digite outro número:"))
soma = n1 + n2

print(f"A soma dos dois números é: {soma}") """

#Exercício de Horas

""" print("Conversão de Horas em Minutos e Segundos")
hora = float(input("Informe a Hora:"))

min = int(hora*60)
seg = min*60

print(f"A hora digitada tem {min} minutos")
print(f"A hora digitada tem {seg} segundos") """

#Exercício da área

""" print("Cálculo de Área")
b = float(input("Insira a base do Retângulo:"))
h = float(input("Insira a Altura do Retângulo:"))

res = b*h

print(f"O Retângulo de Base {b} e Altura {h} tem Área de {res}!") """

""" impostos = ["MEI","Simples"]
for i, imposto in enumerate (impostos):
    print(i,imposto) """



""" frutas = ["mangA", "amora", "morango", "kiwi", "melancia"]
for f in frutas:
    if f.endswith("a") or f.endswith("A"):
        print(f)
        print("Termina com A \n")
    else:
        print(f)
        print("Não termina com A \n") """

#Tupla + Contagem *Obs.: Tuplas não permitem alteração dos valores contidos dentro dela. (Não se pode editar, excluir e nem incluir elementos em uma tupla)

tupla = (2, 1, 4, 3, 7, 5, 6, 8, 9, 22)

print(f'O número 2 apareceu {tupla.count(2)} vezes.')

#Tupla + Index - Mostra a posição índice do elemento a ser procurado

tupla = (2, 1, 4, 3, 7, 5, 6, 8, 9, 22)

print(f'O número 2 apareceu no índice: {tupla.index(9)}.')

#Tupla + Max e Min - Valores máximos e mínimos de uma Tupla

tupla = (2, 1, 4, 3, 7, 5, 6, 8, 9, 22)

print(f'O número mínimo é: {min(tupla)}.')
print(f'O número máximo é: {max(tupla)}.')