frase = str(input('Digite uma frase: ')).upper().strip()
print(f'A letra A aparece {frase.count('A')} vezes na frase.')
print(f'A primeira letra a apareceu na posição {frase.find('A') + 1}')
print(f'a última letra A apareceu na posição {frase.rfind('A') + 1}')