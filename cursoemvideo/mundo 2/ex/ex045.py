from random import choice

print('Vamos jogar jokenpô!')
jogador = str(input('Escolha pedra, papel ou tesoura: '))
jokenpo = ['pedra', 'papel', 'tesoura']
computador = choice(jokenpo)

print(f'Jogador jogou {jogador}\nComputador jogou {computador}')

if jogador == 'pedra': 
    if computador == 'papel': 
        print(f'COMPUTADOR VENCEU!')
    elif computador == 'tesoura':
        print(f'JOGADOR VENCEU!')
    else: 
        print(f'EMPATAMOS!')
elif jogador == 'papel': 
    if computador == 'tesoura': 
            print(f'COMPUTADOR VENCEU!')
    elif computador == 'pedra':
        print(f'JOGADOR VENCEU!')
    else: 
        print(f'EMPATAMOS!')
elif jogador == 'tesoura': 
    if computador == 'pedra': 
            print(f'COMPUTADOR VENCEU!')
    elif computador == 'papel':
        print(f'JOGADOR VENCEU!')
    else: 
        print(f'EMPATAMOS!')
