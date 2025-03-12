"""Exercicio 9"""
altura = float(input('Digite sua altura em metros (ex 1.80 metros):'))
peso = float(input('Digite seu peso em Quilogramas (ex 75.800 Kg)'))
imc = peso / (altura * altura)
if imc < 18.5:
    print(f'Seu imc é {imc:.2f} que é considerado magreza')
elif 18.5 <= imc <= 24.9:
    print(f'Seu imc é {imc:.2f} que é considerado normal')
elif 25.0 <= imc <= 29.9:
    print(f'Seu imc é {imc:.2f} que é considerado sobrepeso')
elif 30.0 <= imc <= 39.9:
    print(f'Seu imc é {imc:.2f} que é considerado obesidade')
else:
    print(f'Seu imc é {imc:.2f} que é considerado obesidade grave')