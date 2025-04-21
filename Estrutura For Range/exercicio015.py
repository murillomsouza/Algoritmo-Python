#Exercicio 15
soma = 1
zero = 0
positivo = 0
negativo = 0
for i in range(0, 10, 1):
    num = float(input(f'Digite o {i + 1}° número: '))
    if num == 0:
        zero += soma
    elif num > 0:
        positivo += soma
    else:
        negativo += soma
print (f'A quantidade de números positivos digitados foi de {positivo}')
print (f'A quantidade de números negativos digitados foi de {negativo}')
print (f'A quantidade de números zeros digitados foi de {zero}')
