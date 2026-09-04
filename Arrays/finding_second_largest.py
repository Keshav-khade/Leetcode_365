# nums = [1, 2, 3, 4, 5]
# nums=[-5, -2, -10, -1]
# nums = [7, 7, 7, 7]
# nums = [-3, 5, -1, 8, 0]
# nums = [10]
# nums = [-1, 0, 1]
# nums = [10, 5, 8, 2, 7]
nums = [5, 5, 4, 4, 3]
# nums = [-5, -2, -10, -1]

"""
# it might improve a little

max_ele = nums[0] # jst for assumption
for i in range(1,len(nums)):
          if nums[i] > max_ele:
                  max_ele = nums[i]

second_largest = float('-inf')
for i in range(len(nums)):
        if nums[i] < max_ele and nums[i] > second_largest:
                second_largest = nums[i]

print(second_largest)
"""

"""
# slitely better approach

largest = float('-inf')
second_largest = float('-inf')

for num in nums:
          if num > largest:
                  second_largest = largest
                  largest = num
          elif num > second_largest and num != largest:
                  second_largest = num

print(second_largest)
"""

"""
for minimum it's also same

smallest = float('inf')
second_smallest = float('inf')

for num in nums:
    if num < smallest:
        second_smallest = smallest
        smallest = num

    elif num < second_smallest and num != smallest:
        second_smallest = num

"""
