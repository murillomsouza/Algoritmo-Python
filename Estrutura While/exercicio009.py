#Exercicio 9 
limite = range(0, 100)
while True:
    sensor = float(input('Digite o valor que aparece no sensor: '))
    if sensor not in limite:
        print('O valor está fora do limite aceitavel! Verifique o ocorrido!')
        break
    else:
        print('Valor dentro do limite estipulado, prossiga com as operações.')
    