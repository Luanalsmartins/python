"""
Leia um valor inteiro N que é a quantidade de 
casos de teste que vem a seguir. Cada caso de 
teste consiste de dois inteiros X e Y. Você deve 
apresentar a soma de Y ímpares consecutivos a 
partir de X inclusive o próprio X se ele for ímpar.
Por exemplo:
para a entrada 4 5, a saída deve ser 45, que é 
equivalente à: 5 + 7 + 9 + 11 + 13
para a entrada 7 4, a saída deve ser 40, que é 
equivalente à: 7 + 9 + 11 + 13

Entrada
A primeira linha de entrada é um inteiro N que é a 
quantidade de casos de teste que vem a seguir. 
Cada caso de teste consiste em uma linha contendo 
dois inteiros X e Y.

Saída
Imprima a soma dos consecutivos números ímpares a 
partir do valor X.
"""

N = int(input())


for i in range(N):
    X, Y = input().split()
    X, Y = int(X), int(Y)
    impar = 0
    qtd_impar = 0 
    while qtd_impar < Y:
        if X % 2 != 0:
            impar += X
            qtd_impar += 1
        X += 1
    print(impar)
