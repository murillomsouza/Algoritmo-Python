#Exercicio 19
import random
choice = random.randrange (1, 10)
print('==========JOGO DO ADIVINHA========== \n Este jogo consiste em o computador escolher 1 número entre 1 e 10 e VOCÊ tentar adivinhar que número é esse  \n =========REGRAS========= \n 1 - Você terá 3 tentativas para acertar \n 2 - Os números estão exclusivamente entre 1 e 10 \n 3 - Caso tente um número que não esteja na sequência você perderá 1 cahnce \n 4 - Por ultimo e não menos importante, divirta-se!!')
for i in range (0, 3, 1):
    num =  int(input('Tente advinhar o número de 1 a 10: '))
    if num > choice:
        print(f'O número escolhido é menor que {num}, tente novamente')
    elif num < choice:
        print(f'O número escolhdo é maior que {num}, tente novamente')
    elif num == choice:
        print(f'Parabéns você acertou! O número escolhido era {choice}!')
        break
    else:
        print('Número inválido, o número está entre 1 e 10.')

