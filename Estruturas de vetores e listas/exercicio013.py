#Leia uma lista de números e crie uma nova lista apenas com os valores únicos (sem repetições).
lista = [7, 3, 5, 2, 7, 9, 3, 1, 4, 5, 8, 6, 2, 10, 3, 7, 6, 4, 9, 1]
numeros = []
for i in lista:
    if i not in numeros:
        numeros.append(i)
print(f'A lista sem repetir números fica da sequinte forma: {numeros}')

