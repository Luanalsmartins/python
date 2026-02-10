inicio, fim = input().split()

inicio = int(inicio)
fim = int(fim)

if inicio == fim:
    print('O JOGO DUROU 24 HORA(S)')
elif inicio > fim:
    duracao_jogo = (fim - inicio + 24)
    print(f'O JOGO DUROU {duracao_jogo} HORA(S)')
else:
    duracao_jogo = fim - inicio
    print(f'O JOGO DUROU {duracao_jogo} HORA(S)')