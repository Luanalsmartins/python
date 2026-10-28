from random import randint

comp = randint(0, 10)

print('-*' * 30)
print('Vou pensar em um número entre 0 e 10, tente adivinhar!')
print('-*' * 30)

c = 1
num = int(input('Digite seu número: '))

while num != comp:
    if num > 10:
        print('Digite um número entre 0 e 10!')
    elif num < comp:
        print('Mais... Tente novamente!')
    elif num > comp:
        print('Menos... Tente novamente!')
    c += 1
    num = int(input('Digite seu número: '))
print(f'Parabéns, o número sorteado foi {comp}, você acertou em {c} palpites.')