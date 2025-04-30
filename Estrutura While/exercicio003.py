#Exercicio 3
acum_positiv = 0
acum_negativ = 0
zeros = 0
while True:
    entrada = input("Digite um número (ou 'sair' para encerrar): ")
    if entrada.lower() == 'sair':
        break
    try:
        numero = float(entrada)
        if numero > 0:
            acum_positiv += 1
        elif numero < 0:
            acum_negativ += 1
        else:
            zeros += 1
    except ValueError:
        print("Entrada inválida. Por favor, digite um número ou 'sair'.")
print(f"Positivos: {acum_positiv}")
print(f"Negativos: {acum_negativ}")
print(f"Zeros: {zeros}")
