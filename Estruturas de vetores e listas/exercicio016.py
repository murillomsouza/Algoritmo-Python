# Junte duas listas e remova os elementos repetidos.
lista1 = [4, 17, 2, 10, 8, 3, 6, 12, 7, 14]
lista2 = [8, 1, 3, 10, 9, 5, 14, 6, 13, 11]
filtro = []
for i in lista1 and lista2:
    if i not in filtro:
        filtro.append(i)
filtro.sort()
print(filtro)