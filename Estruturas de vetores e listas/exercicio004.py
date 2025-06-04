# Some todos os elementos de uma lista de inteiros digitados pelo usuário.
lista = []
for i in range(10):
    num = int(input(f'Digite o {i+1}º número: '))
    lista.append(num)
print(f'Os numeros digitados foram: {sum(lista)}')