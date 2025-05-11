#Exercicio 12
estoque = 100
while estoque > 0: 
    venda = int(input('Digite a quantidade que está sendo vendida: '))
    if venda > estoque:
        print('Quantidade inválida, tente novamente')
    else:
        estoque -= venda
        print(f'Venda realizada com sucesso. O estoque atual contém {estoque} itens.')
print('O estoque já está esgotado e você não pode mais realizar essa operação')
