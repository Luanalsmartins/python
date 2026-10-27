pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 1
qt = 11

while c <= qt-1:
    print(f'{pt} ', end='')
    pt += r
    c += 1
    if c == qt:
        mt = str(input('Você deseja exibir mais alguns termos? Digite a quantidade desejada ou 0 para encerrar o programa: '))
        if mt != 0:
            qt == mt
            print(f'{pt}', end='')
            pt += r
            c += 1
print('FIM')