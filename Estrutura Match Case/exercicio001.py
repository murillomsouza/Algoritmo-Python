#-----Exercicio 1-----
#-----Moedas utilizadas-----
usd = 5.73
eur = 6.18
gbp = 7.35

#-----Seleção de moeda-----
moeda = input('Digite a moeda que você que deseja converter. \n Para Dolár (USD) digite 1,\n Para Euro (EUR) digite 2,\n Para Libra (GBP) digite 3.\n Digite 4 para sair')
real = float(input('Digite o valor em Reais (BRL) a ser convertido: '))
match moeda:
    case "1":
        print(f'O total após a conversão é de U${real / usd:.2}')
    case "2":
        print(f'O total após a conversão é de €{real / eur:.2}')
    case "3":
        print(f'O total após a conversão é de £{real / gbp:.2}')
    case "4":
        print('Obrigado por usar o conversor de moedas! Volte sempre')
    case _:
        print('opção inválida.')
