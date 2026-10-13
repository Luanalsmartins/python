from math import hypot
cat_op = float(input("Digite o comprimento do cateto oposto: "))
cat_adj = float(input("Digite o comprimento do cateto adjacente: "))
hipotenusa = hypot(cat_op, cat_adj)
print("O comprimento da hipotenusa é {:.2f}".format(hipotenusa))
