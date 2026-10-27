pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 1

while c <= 10:
    print(f'{pt} ', end='')
    pt += r
    c += 1
print('FIM')