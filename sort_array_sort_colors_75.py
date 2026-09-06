"""
You are given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
"""

# you can solve this problem using Dutch national flag algorithm

"""
# using bubble sort / O(n^2)
nums = [2,0,2,1,1,0]
n = len(nums)
for i in range(n-1):
          for j in range(1, n):
                  if nums[j] < nums[j-1]:
                          temp = nums[j]
                          nums[j] = nums[j-1]
                          nums[j-1] = temp
print(nums)
"""

"""
# using sort() / O(n log n)
nums = [2,0,2,1,1,0]
nums.sort()

in-place sorting function provided by psf
"""


"""
# using frequency count and then feeding that resultant array

# count all the 0's 1's and 2's

nums = [2,0,2,1,1,0]
count_0 = 0
count_1 = 0
count_2 = 0
for i in range(len(nums)):
          if nums[i] == 0:
                  count_0 += 1
          elif nums[i] == 1:
                  count_1 += 1
          else:
                  count_2 += 1
i = 0
for _ in range(count_0):
        nums[i] = 0
        i += 1
      
for _ in range(count_1):
        nums[i] = 1
        i += 1

for _ in range(count_2):
        nums[i] = 2
        i += 1

print(nums)
"""



"""
# using Dutch national flag algorithm / o(n) / O(1)
nums = [2,0,2,1,1,0]

low = 0
mid = 0
high = len(nums) - 1

while mid <= high:
          if nums[mid] == 0:
                    temp = nums[low]
                    nums[low] = nums[mid]
                    nums[mid] = temp
                    low += 1
                    mid += 1
          elif nums[mid] == 1:
                  mid += 1
          else:
                  temp = nums[mid]
                  nums[mid] = nums[high]
                  nums[high] = temp
                  high -= 1

print(nums)

"""

