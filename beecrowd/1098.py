i = 0

while i <= 2:
    j = 1
    while j <= 3.0:
        if i == 1 or i >= 1.9 and i <= 2.1:
            print(f'I={i:.0f} J={j + i:.0f}')
        else:
            print(f'I={round(i,1)} J={round(j + i,1)}')
        j += 1
    i += 0.2