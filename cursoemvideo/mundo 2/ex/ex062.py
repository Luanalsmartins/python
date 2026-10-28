pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 1
c2 = 1

while c <= 10:
    print(f'{pt} ', end='')
    pt += r
    c += 1
    if c == 11:
        mt = int(input('\nVocê deseja exibir mais alguns termos? Digite a quantidade desejada ou 0 para encerrar o programa: '))
        if mt != 0:
            while c2 <= mt:
                print(f'{pt} ', end='')
                pt += r
                c2 += 1
print('FIM')