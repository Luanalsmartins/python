peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura**2)
print(f'O IMC dessa pessoa é de {imc:.2f}.')

if imc < 18.5:
    print('Vocẽ está ABAIXO do peso ideal.')
elif imc >= 18.5 and imc < 25:
    print('Você está no peso IDEAL.')
elif imc >= 25 and imc < 30:
    print('Você está SOBREPESO.')
elif imc >= 30 and imc <= 40:
    print('Você está na OBESIDADE, cuidado.')
else:
    print('Você está na OBESIDADE MÓRBIDA, cuidado.')
