# nums = [1, 2, 3, 4, 5]
nums=[-5, -2, -10, -1]
# nums = [7, 7, 7, 7]
# nums = [-3, 5, -1, 8, 0]
# nums = [10]
# nums = [-1, 0, 1]

"""

#using iterative approach
max_ele = nums[0] # jst for assumption
for i in range(1,len(nums)):
          if nums[i] > max_ele:
                  max_ele = nums[i]
print(max_ele)

"""

"""

# using this app. sort -> whoever the largest would go to last
nums.sort()
n = len(nums)
largest = nums[n-1]
print(largest)

"""