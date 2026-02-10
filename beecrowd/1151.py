def fibonacci(n):
    a, b = 0, 1 
    result = []
    for _ in range(n):
        result.append(a) # armazena o valor de a na lista
        a, b = b, a + b # a passa a ser b e b passa a ser a+b 

    print(' '.join(map(str, result)))

n = int(input())
fibonacci(n)
