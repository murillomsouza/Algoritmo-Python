#Exercicio 6
soma = 0
cont = 0
while True:
    nota = int(input('Digite a nota: '))
    if nota < 0:
        break
    elif nota < 11:
      soma += nota
      cont += 1
    else:
        print('Nota inválida, digite números de 1 a 10')
print(f'A média das notas é de {soma / cont}')