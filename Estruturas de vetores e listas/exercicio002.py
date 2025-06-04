# Peça ao usuário para digitar 5 nomes e armazene-os em uma lista. Depois, exiba os nomes um por um.
lista_nomes = []
for i in range(5):
    nomes = input('Digite um nome:')
    lista_nomes.append(nomes)
print(lista_nomes)