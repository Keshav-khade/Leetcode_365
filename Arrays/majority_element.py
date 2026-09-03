# algorithm boyer moore's voting algorithm 

from typing import *

# time limit exceeded for 50k element array. time complexity is O(n^2)
def majorityElement1(nums: List[int]) -> int:
          for i in range(len(nums)):
                    count = 1
                    for j in range(i+1, len(nums)):
                            if nums[i] == nums[j]:
                              count += 1
                    if count > len(nums) // 2:
                              return nums[i]
# # nums = []
# # nums = [8,8,7,7,7]
# # nums = [2,2,3,3,3,3,2]
# res = majorityElement(nums)
# print(res)

# better approach with hashmap in python it's called dictionary
def majorityElement2(nums: List[int]) -> int:
          d = dict()

          for i in range(len(nums)):
                    if nums[i] in d:
                              d[nums[i]] = d.get(nums[i],0) + 1
                    else:
                              d[nums[i]] = 1

          for key,val in d.items():
                  if val > len(nums)//2:
                          return key

# # nums = [2,2,3,3,3,3,2]
# nums = [8,8,7,7,7]
# res = majorityElement2(nums)
# print(res)

# optimal approach time o(n) and space o(1) with boyer moore's algorithm
def majorityElement3(nums: List[int]) -> int:
          candidate = None
          count = 0
          for num in nums:
                    if count == 0:
                            candidate = num

                    if candidate == num:
                            count += 1
                    else:
                            count -= 1
          return candidate

# nums = [2,2,3,3,3,3,2]
nums = [8,8,7,7,7]
res = majorityElement3(nums)
print(res)