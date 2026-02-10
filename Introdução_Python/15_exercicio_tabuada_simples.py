# Receba um número inteiro do usuário e mostre a tabuada desse número

numero = int(input('Digite qual número deseja saber a tabuada: '))
i = 1
while i <= 10:
    print(f'{numero} x {i} = {numero*i}') # Mostra o numero que o usuário escolheu depois o número peloo qual está sendo multiplicado e depois o resultado da multiplicação
    i += 1 # incrementa 1 no i 