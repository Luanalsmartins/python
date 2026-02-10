a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

if a < b and a < c and b < c:
    print(f'{a}\n{b}\n{c}\n') 
    print(f'{a}\n{b}\n{c}')
elif a < b and a < c and c < b:
    print(f'{a}\n{c}\n{b}\n')
    print(f'{a}\n{b}\n{c}')
elif b < a and b < c and a < c:
    print(f'{b}\n{a}\n{c}\n')
    print(f'{a}\n{b}\n{c}')
elif b < a and b < c and c < a:
    print(f'{b}\n{c}\n{a}\n')
    print(f'{a}\n{b}\n{c}')
elif c < a and c < b and a < b:
    print(f'{c}\n{a}\n{b}\n')
    print(f'{a}\n{b}\n{c}')
elif c < a and c < b and b < a: 
    print(f'{c}\n{b}\n{a}\n')
    print(f'{a}\n{b}\n{c}')