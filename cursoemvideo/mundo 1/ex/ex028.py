import random
from time import sleep
computador = random.randint(0, 5)
print('-*' * 30)
print('Vou pensar em um número entre 0 e 5, tente adivinhar!')
print('-*' * 30)

num = int(input('Digite seu número! '))
print('PROCESSANDO...')
sleep(2)
if num == computador: 
    print(f'Parabéns, vocẽ acertou! O número sorteado foi {computador}')
else: 
    print(f'Não foi dessa vez! O número sorteado foi {computador}')
