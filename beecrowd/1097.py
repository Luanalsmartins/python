i = 1

while i <= 9:
    j_start = i + 6
    j = j_start
    while j >= j_start - 2:
        print(f'I={i} J={j}')
        j-=1
    i+=2


'''	
I=1 J=7
I=1 J=6
I=1 J=5
I=3 J=9
I=3 J=8
I=3 J=7
...
I=9 J=15
I=9 J=14
I=9 J=13
'''