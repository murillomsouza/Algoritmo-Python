#-----Exercicio 7-----
operador = input('Digite a operação que deseja fazer: \n + \n - \n / \n * \n')
match operador:
    case'+':
        numero1 = float(input('Digite o primeiro numero: '))
        numero2 = float(input('Digite o segundo numero: '))
        print(f'A soma deles é {numero1 + numero2}')
    case '-':
        numero1 = float(input('Digite o primeiro numero: '))
        numero2 = float(input('Digite o segundo numero: '))
        print(f'A subtração deles é {numero1 - numero2}')
    case '/':
        numero1 = float(input('Digite o primeiro numero: '))
        numero2 = float(input('Digite o segundo numero: '))
        print(f'A divisão deles é {numero1 / numero2}')
    case '*':
        numero1 = float(input('Digite o primeiro numero: '))
        numero2 = float(input('Digite o segundo numero: '))
        print(f'A multiplicação deles é {numero1 * numero2}')
    case _:
        print('Opção inválida.')