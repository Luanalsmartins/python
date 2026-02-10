# Receba uma temperatura em farenheit e exiba em graus celsius. 
# C = 5 / 9 * (f - 32)

temperatura_farenheit = float(input('Digite a temperatura em graus Farenheit: '))

temperatura_celsius = 5/9 * (temperatura_farenheit - 32)
"""temperatura_celsius = 5 * ((temperatura_farenheit-32)/9)"""

print(f'A temperatura em graus Celsius é: {temperatura_celsius:.2f}°C')