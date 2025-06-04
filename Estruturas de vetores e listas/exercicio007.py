# Faça um programa que leia 10 números e armazene em duas listas: uma com pares e outra com ímpares.
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
impares = []
pares = []
for num in lista:
    if num % 2 == 0: pares.append(num)
    else: impares.append(num)
print(f'Lista impar: {impares}, \nlista par: {pares}.')
