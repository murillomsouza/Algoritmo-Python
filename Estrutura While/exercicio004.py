#Exercicio 4
temp = {}
while temp != 0:
    temp = float(input('Digite a temperatura que será convertida: '))
    conversao = (temp * 1.8) + 32
    print(f'A temperatura em Fahrenheit é de {conversao}')
    if temp == 0:
        print(f'A conversão em Fahrenheit é de {conversao}.')
        break
