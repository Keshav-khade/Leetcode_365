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
nums = [1, 2, 2, 1]

flag = True
for i in range(1, len(nums)):
          if nums[i] >= nums[i-1]:
                  flag = True
          else:
                  flag = False
                  break

print(flag)