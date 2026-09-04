"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

# nums = [0,1,0,3,12]
# nums = [0, 1, 0, 3, 12]
# nums = [1, 0, 2, 0, 3]
# nums = [1, 2, 3, 0, 0]
# nums = [0, 0, 1, 2, 3]

# nums = [1, 0, 0, 2, 0, 3]
# nums = [0, 0, 0, 0]
# nums = [1, 2, 3, 4]
# nums = [0]
# nums = [0, 1, 0, 0, 2, 0, 3]
nums = [-1, 0, -2, 3, 0, 4]

i = 0
for j in range(len(nums)):
          # non-zero keep it , zero keep it at last
          if nums[j] != 0:
                  nums[i] = nums[j]
                  i += 1
for j in range(i,len(nums)):
        nums[j] = 0


# time o(n) and space o(1)
i = 0
for j in range(len(nums)):
        if nums[j] != 0:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1

print(nums)