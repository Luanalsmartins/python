from random import choice

escolha = ['par', 'ímpar']
num_pc = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s = c = 0
ganhou = ''

while True:
    valor_jogador = int(input('Digite um valor: '))
    jogador = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    valor_pc = choice(num_pc)
    pc = choice(escolha)
    s = valor_jogador + valor_pc
    if s % 2 == 0:
        ganhou = 'PAR'
    else:
        ganhou = 'ÍMPAR'

    print(f'Você jogou {valor_jogador} e o computador {valor_pc}. Total de {s} DEU {ganhou}')
    if jogador in 'Pp' and ganhou == 'PAR' or jogador in 'Ii' and ganhou == 'ÍMPAR':
        print('Você VENCEU!')
        c += 1
    else:
        print('Você PERDEU!')
        print(f'GAME OVER! Você venceu {c} vezes.')
        break