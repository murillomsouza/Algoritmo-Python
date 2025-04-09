#Exercicio 10
num = int(input('Digite o numero factorial: '))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f'O resultado é {factorial}')
