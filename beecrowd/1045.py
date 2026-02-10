def ordenar_lados_decrescente(A, B, C):
    lados = [A, B, C]

    lados_ordenados = sorted(lados, reverse = True)

    A, B, C = lados_ordenados
    return A, B, C

A, B, C = input().split()

A = float(A)
B = float(B)
C = float(C)

A, B, C = ordenar_lados_decrescente(A, B, C)


if A >= B + C:
    print('NAO FORMA TRIANGULO')
else:
    if A**2 == B**2 + C**2:
        print('TRIANGULO RETANGULO')
    if A**2 > B**2 + C**2:
        print('TRIANGULO OBTUSANGULO')
    if A**2 < B**2 + C**2:
        print('TRIANGULO ACUTANGULO')
    if A == B == C:
        print('TRIANGULO EQUILATERO')
    if A == B and B != C or A == C and A != B or B == C and A != C:
        print('TRIANGULO ISOSCELES')