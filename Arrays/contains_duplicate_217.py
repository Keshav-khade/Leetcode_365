"""
leetcode 217
"""

"""
# extreme brute force approach got TLE

duplicate = False
n = len(nums)
for i in range(n):
          cou = 1
          for j in range(i+1, n):
                    if nums[i] == nums[j]:
                          cou += 1
          if cou > 1:
                  duplicate = True
                  print("True")
                  break
if not duplicate:
          print("false")
"""


"""
# better approach for improvement / final solution O(n) O(n)

d = {}
for num in nums:
          if num not in d:
                  d[num] = 1
          else:
                  d[num] = d.get(num, 0) + 1
for j in d.values():
        if j > 1:
          print("True")
          break

"""

"""
# got TLE

def duplicate(nums):
          for num in nums:
                    if nums.count(num) > 1:
                          return True
          return False
                  
nums = [1,2,3]
res = duplicate(nums)
print(res)
"""