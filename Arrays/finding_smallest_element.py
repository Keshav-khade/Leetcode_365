# nums = [1, 2, 3, 4, 5]
# nums=[-5, -2, -10, -1]
# nums = [7, 7, 7, 7]
# nums = [-3, 5, -1, 8, 0]
# nums = [10]
nums = [-1, 0, 1]

min_ele = float('inf') # jst for assumption
for i in range(len(nums)):
          if nums[i] < min_ele:
                  min_ele = nums[i]

print(min_ele)