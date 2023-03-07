#Função
""" def soma(a,b):
    return a+b

print(soma(2,9))
soma(7,8)
soma(10,15) """

# Função 1
""" def pesquise(lista, valor):
    for x,e in enumerate(lista):
        if e == valor:
            return x
    return None

L = [10, 20, 25, 30]
print(pesquise(L, 25))
print(pesquise(L, 27)) """

#Função 2
L = [10, 15, 20, 25]
def soma(L):
    total = 0
    for e in L:
        total += e
    return total
def media(L):
    return(soma(L)/len(L))

print(soma(L))