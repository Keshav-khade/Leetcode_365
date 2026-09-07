# # 1 way to solve this problem
# n = int(input("enter a number"))
# if n >= 0:
#     if n%2 == 0:
#         print('even')
#     else:
#         print('odd')
# else:
#     print('invalid')


# # using bitwise operator
# n = int(input("enter a number"))
# if n < 0:
#     print("invalid")
# else:
#     if n & 1 == 0:
#         print("even")
#     elif n & 1 == 1:
#         print("odd")


# # 3rd way of doing it
# n = int(input())
# print('invalid' if n < 0 else 'even' if n%2 == 0 else 'odd')

# way 4 for same problem
n = int(input("Enter a number: "))
q = n // 2
if q*2 == n:
    print("even")
else:
    print("odd")