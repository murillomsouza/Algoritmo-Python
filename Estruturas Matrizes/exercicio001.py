# Crie uma matriz 3x3 com valores digitados pelo usuário.
linha = 3
coluna = 3
matriz = []
for i in range(linha):
    linha = []
    for j in range(coluna):
        num = int(input(f'Adicione um número a matriz [{i}] [{j}]: '))
        linha.append(num)
    matriz.append(linha)
for linha in matriz:
    print(linha)