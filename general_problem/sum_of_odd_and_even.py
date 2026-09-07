# first is for even only
print(sum([int(i) for i in list(input()) if int(i)%2 == 0]))

# second is for only odd's 
print(sum([int(i) for i in list(input()) if int(i)%2 != 0]))