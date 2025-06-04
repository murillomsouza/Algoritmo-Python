# Remova todos os números negativos de uma lista de inteiros.
numeros = [12, -5, 8, 0, -13, 7, -2, 19, -8, 3, -21, 6, 14, -1, 9, -7, 11, -12, 5, -4, 2, -9, 17, -6, 1, -3, 10, -11, 4, -10]
for i in numeros:
    if i < 0:
        numeros.remove(i)
print(numeros)
