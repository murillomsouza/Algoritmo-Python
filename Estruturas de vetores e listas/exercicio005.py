# Conte quantas vezes o número 3 aparece em uma lista.
lista = [8, 3, 5, 3, 1, 3, 9, 7, 3, 6, 3, 4, 3, 2, 3, 10, 3, 3, 0, 3]
cont = 0
for i in lista:
    if i == 3:
        cont+= 1
print(f'Na sequinte lista \n{lista} \n O Número 3 apareceu {cont} vezes na lista')
