n = int(input("enter a number: "))

sum = 0
while n != 0:
    d = n % 10
    sum += d
    n = n // 10
print(sum)


# 2 way using list comprehension
print(sum(int(i) for i in list(input())))