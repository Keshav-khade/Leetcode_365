"""

You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

You should return the array of nums such that the array follows the given conditions:

Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

"""

"""
nums = [3,1,-2,-5,2,-4]

positive = []
negative = []
resultant = []
for i in range(len(nums)):
          if nums[i] < 0:
                    negative.append(nums[i])
          else:
                    positive.append(nums[i])
# n = min(len(positive),len(negative))
# n = len(positive)
for i in range(len(positive)):
        resultant.append(positive[i])
        resultant.append(negative[i])

print(resultant)
"""

"""
nums = [3,1,-2,-5,2,-4]
resultant = [0]*len(nums)

p = 0
n = 1
for i in range(len(nums)):
          if nums[i] < 0:
                    resultant[n] = nums[i]
                    n += 2
          else:
                    resultant[p] = nums[i]
                    p += 2

print(resultant)
"""
