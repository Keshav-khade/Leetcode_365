# nums = [1, 2, 3, 4, 5]
# nums = [5, 4, 3, 2, 1]
# nums = [1, 1, 2, 3, 4]
# nums = [1]
# nums = []

# nums = [-5, -3, -1, 0, 4]
# nums = [-5, -3, -4, 0, 4]
# nums = [-1, 0, 0, 2, 5]

# nums = [1, 2, 4, 3, 5]
# nums = [1, 3, 2]
# nums = [10, 20, 30, 25, 40]
# nums = [1, 2, 3, 3, 4, 5]
# nums = [5, 5, 5, 5]
# nums = [2, 1]
# nums = [1, 2, 2, 1]

"""
# how to check if array is sorted
flag = True
for i in range(1, len(nums)):
          if nums[i] >= nums[i-1]:
                  flag = True
          else:
                  flag = False
                  break
print(flag)
"""

"""
# how to check if given array is sorted and rotated / O(n^2) brute force

# from left -> 2
# from right -> 3
# original = [3,4,5,1,2]
# original = [2,1,3,4]
original = [1,2,3]

# sort the given array first
copy_original = original.copy()

copy_original.sort()

n = len(copy_original)
flag = False
for _ in range(n):
        temp = copy_original[0]
        for i in range(1, n):
                copy_original[i-1] = copy_original[i]
        copy_original[n-1] = temp

        if copy_original == original:
                flag = True
                print("your arr is sorted and rotated !")
                break
if not flag:
        print("your arr is not sorted & rotated !")
"""

"""
# it's slitely better approach without using math

nums = [1,2,3]
n = len(nums)
count = 0
for i in range(n):
        if i == n-1:
                if nums[i] > nums[0]:
                        count += 1
                        break
                else:
                        break
        if nums[i] > nums[i+1]:
                count += 1

if count == 1:
        print("your arr is sorted and rotated !")
else:
        print("it's not")
"""


"""
# with using math and taking advantage of modulo operator and index wrapping

# nums = [3,4,5,1,2]
# nums = [2,1,3,4]
nums = [1,2,3]
n = len(nums)
count = 0
for i in range(n):
        if nums[i] > nums[(i+1)%n]:
                count += 1

if count <= 1:
        print("your arr is sorted and rotated !")
else:
        print("it's not")

"""
