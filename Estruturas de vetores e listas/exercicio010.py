# Faça um programa que leia números do usuário até que ele digite 0. Depois, mostre a lista e a soma dos números.
soma = []
while True:
    num = float(input('Digite o número a ser somado: '))
    if num == 0:
        break
    else:
        soma.append(num)
print(f'A soma dos números digitados é de {sum(soma)}')

