# Dessa forma o programa roda infinitamente, sem o brake ele não para!
'''c = 1
while True:
    print(c,'->', end='')
    c += 1
print('Acabou')'''

n = s = 0

while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')