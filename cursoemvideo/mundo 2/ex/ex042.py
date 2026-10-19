r1 = int(input('Digite o valor da reta número 1: '))
r2 = int(input('Digite o valor da reta número 2: '))
r3 = int(input('Digite o valor da reta número 3: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    if r1 == r2 == r3:
        print('Os seguimentos acima podem formar um Triângulo Equilátero.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Os seguimentos acima podem formar um Triângulo Isósceles.')
    else:
        print('Os seguimentos acima podem formar um Triângulo Escaleno.')
else:
    print('Com esse valores, não conseguimos formar um triângulo!') 