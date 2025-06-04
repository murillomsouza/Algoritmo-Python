# Substitua todos os números ímpares de uma lista por zero.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in numeros:
    if i % 2 != 0:
        numeros.remove(i)
        numeros.append(0)
print(f'A lista atualizada: {numeros}')