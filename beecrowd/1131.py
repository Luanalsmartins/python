qtd_grenais = 1
qtd_inter = 0
qtd_gremio = 0
empate = 0
while True: 
    inter, gremio = input().split()
    inter = int(inter)
    gremio = int(gremio)
    if inter > gremio:
        qtd_inter += 1
    elif gremio > inter:
        qtd_gremio += 1
    elif inter == gremio:
        empate += 1
    print('Novo grenal (1-sim 2-nao)')
    novo_grenal = int(input())
    if novo_grenal == 1:
        qtd_grenais += 1
        continue
    elif novo_grenal == 2:
        print(f'{qtd_grenais} grenais')
        print(f'Inter:{qtd_inter}')
        print(f'Gremio:{qtd_gremio}')
        print(f'Empates:{empate}')
        if qtd_inter > qtd_gremio:
            print('Inter venceu mais')
        elif qtd_gremio > qtd_inter:
            print('Gremio venceu mais')
        break
