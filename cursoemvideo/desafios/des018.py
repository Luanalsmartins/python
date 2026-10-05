import math
ang = float(input("Digite o valor do ângulo: "))
ang_rad = math.radians(ang)
seno = math.sin(ang_rad)
cosseno = math.cos(ang_rad)
tangente = math.tan(ang_rad)
print("O valor de seno é {:.2f}\nO valor de cosseno é {:.2f}\nO valor da tangente é {:.2f}".format(seno, cosseno, tangente))