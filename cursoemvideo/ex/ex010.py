real = float(input("Quanto dinheiro você tem na sua carteira? R$"))
dolar = 3.27
print("Com R${:.2f} você pode comprar U${:.2f}".format(real, (real/dolar)))