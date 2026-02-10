x = int(input())
z = int(input())

while z <= x :
    z = int(input())

i = 1
aux = x

while x < z:
    x = x + (aux + 1)
    aux += 1
    i += 1
print(i)