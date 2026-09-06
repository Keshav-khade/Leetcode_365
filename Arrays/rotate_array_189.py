"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
# right rotations
"""
from typing import *

# nums = [1,2,3,4,5,6,7]
# k = 3

# nums = [-1,-100,3,99]
# k = 2

"""
# for k = 10^5 , and length of lst is also 10^5 for this input it got TLE
def right_rotate(nums:List , k:int)->None:
          n = len(nums)
          while k > 0:
                    temp = nums[n-1]
                    for i in range(n-1, -1, -1):
                          nums[i] = nums[i-1]
                    nums[i] = temp
                    k -= 1

right_rotate(nums,k)
print(nums)
"""

"""
# slitely better optimization using list slicing / partitioning

nums = [1,2,3,4,5,6,7]
k = 3

result = nums[-k:] + nums[:-k]
print(result)
"""


"""
# try to find in-place solution O(n) / O(1)

class Solution:
def rotate(self, nums: list[int], k: int) -> None:
          def reverse(nums,i,j):
                    while i < j:
                    nums[i],nums[j] = nums[j],nums[i]
                    i += 1
                    j -= 1
          n = len(nums)
          k = k % n
          reverse(nums,0,n-1)
          reverse(nums,0,k-1)
          reverse(nums,k,n-1)
"""

