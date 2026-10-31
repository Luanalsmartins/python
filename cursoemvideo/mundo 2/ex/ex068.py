from random import randint

escolha = ['par', 'ímpar']
vitorias = 0
ganhou = ''

while True:
    valor_jogador = int(input('Digite um valor: '))
    jogador = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    valor_pc = randint(0, 10)
    s = valor_jogador + valor_pc

    if s % 2 == 0:
        ganhou = 'PAR'
    else:
        ganhou = 'ÍMPAR'

    print(f'Você jogou {valor_jogador} e o computador {valor_pc}. Total de {s} DEU {ganhou}')

    if (jogador in 'P' and ganhou == 'PAR') or (jogador in 'I' and ganhou == 'ÍMPAR'):
        print('Você VENCEU!')
        vitorias += 1
    else:
        print('Você PERDEU!')
        print(f'GAME OVER! Você venceu {vitorias} vezes.')
        break