#Exercicio 1
soma = 0
num = float(input('Digite um número a ser somado: '))
while num != 0:
    soma += num
    num = float(input('Digite outro número: '))
print(soma)