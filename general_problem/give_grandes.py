# question no.4

# 1 way
n = int(input())
if n >= 30 and n <= 100:
    if n >= 30 and n <= 50:
        print('D')
    elif n >= 51 and n <= 60:
        print('C')
    elif n >= 61 and n <= 80:
        print('B')
    else:
        print('A')
else:
    print('invalid')
        
# 2nd way
n = int(input())
if n >= 30 and n <= 100:
    if n >= 81:
        print('A')
    elif n >= 61:
        print('B')
    elif n >= 51:
        print('C')
    else:
        print('D')
else:
    print('invalid')