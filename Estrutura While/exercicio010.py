#Exercicio 10
candidato_1 = 0
candidato_2 = 0
candidato_3 = 0
while True:
    decisao = input('O que deseja fazer? \n Digite "votar" para votar ou "fim" para sair.' ).lower()
    match decisao:
        case "votar":
            voto = int(input('Qual candidato você deseja votar? 1, 2 ou 3?'))
            if voto == 1:
                candidato_1 += 1
            elif voto == 2:
                candidato_2 += 1
            elif voto == 3:
                candidato_3 += 1
            else: 
                print('Escolha uma opção disponível, tente novamente.')
                break
        case "fim":
            print(f'Obrigado por votar, o resultado da eleição foi de: \n Candidato 1 recebeu {candidato_1} votos. \n Candidato 2 recebeu {candidato_2} votos. \n Canditado 3 recebeu {candidato_3} votos')