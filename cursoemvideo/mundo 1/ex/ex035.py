r1 = int(input('Digite o valor da reta número 1: '))
r2 = int(input('Digite o valor da reta número 2: '))
r3 = int(input('Digite o valor da reta número 3: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('\033[32;40mCom esse valores conseguimos formar um triângulo!')
else:
    print('\033[31;40mCom esse valores, não conseguimos formar um triângulo!') 