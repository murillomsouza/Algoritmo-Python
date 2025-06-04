# Faça uma função que recebe uma lista e retorna outra com os elementos em ordem reversa (sem usar .reverse() ou [::-1]).
lista = [1, 2, 3, 4, 5, 6]
lista_reversa = []
tamanho = 0
for _ in lista:
    tamanho += 1
i = tamanho - 1
while i >= 0:
    lista_reversa.append(lista[i])
    i -= 1
print(lista_reversa)