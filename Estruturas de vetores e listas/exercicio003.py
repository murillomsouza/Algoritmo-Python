# Crie uma lista com 10 números e mostre apenas os números pares.
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_par = []
for i in lista:
    if i % 2 == 0:
        lista_par.append(i)
print(lista_par)