"""
recursion -> is a type of function which calls itself until it matches the base case or an base condition.

for an instance : ex. for a factorial

def fact(number):
    result = 1
    if number == 0:
        return 1
    result = number *  fact(number-1)

    return result

num = int(input("Enter the number: "))
res = fact(num)
print(res)
"""

def ncr(n,r):
    if r == 0 or r == n:
        return 1
    return ncr(n-1,r-1) + ncr(n-1,r)

res = ncr(4,2)
print(res)

