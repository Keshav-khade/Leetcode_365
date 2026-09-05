from typing import *
"""
There are two methods to rotate an array
1. left rotation
2. right rotation

"""

# rotate an array by 1 to left
def rotate(nums, k) ->  None:
          for _ in range(k):
                    temp = nums[0]
                    n = len(nums)
                    for i in range(1, n):
                              nums[i-1] = nums[i]
                    nums[n-1] = temp

k = int(input("enter how many rotations: "))
nums = [1,2,3,4,5]
rotate(nums,k)  
print(nums)


# right rotation / time complexity o(k*n)
def right_rotate(nums,k):
        for _ in range(k):
                n = len(nums)
                temp = nums[n-1]
                for i in range(n-1,-1,-1):
                        nums[i] = nums[i-1]
                nums[i] = temp

k = int(input("enter how many rotations: "))
nums = [1,2,3,4,5]
right_rotate(nums,k)
print(nums)



# how to improve logic wise approach use slicing here / time complexity O(n) / right rotation approach
k = int(input("enter how many rotations: "))
nums = [1,2,3,4,5]
nums = nums[-k:] + nums[:-k]
print(nums)

# how to rotate it left using slicing
k = int(input("enter how many rotations: "))
nums = [1,2,3,4,5]
nums = nums[k:] + nums[:k]
print(nums)

# ______________________________________________________________________________________________________________

# how to implement in-place solution
# That's the famous three-reversal technique.

def reverse(nums,start,end):
        i = start
        j = end
        while i < j:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
                j -= 1

nums = [1,2,3,4,5]
k = int(input("enter how many rotations: "))
n = len(nums)-1
reverse(nums,0,n)
reverse(nums,0,k-1)
reverse(nums,k,n)

# your final rotate array by place k
print(nums)