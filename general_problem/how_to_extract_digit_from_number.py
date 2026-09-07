n = int(input("enter a number"))

# # 1 way
while n != 0:
          print(n%10,end=' ')
          n = n // 10

# 2 way
for i in input()[::-1]:
        print(i,end=' ')
