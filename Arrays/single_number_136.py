"""
problem statement ->
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

"""
from typing import *
class Solution:
    def singleNumber1(self, nums: List[int]) -> int:
        d = dict()
        for i in nums:
            if i in d:
                d[i] = d.get(i, 0) + 1
            else:
                d[i] = 1
        
        val = 0
        ans = 0
        for i in nums:
            if i == val:
                continue
            if d.get(i,0) == 1:
                ans = i
                break
        return ans

    # using xor operator
    def singleNumber2(self, nums: List[int]) -> int:
            ans = 0 
            # it won't affect anything because of a ^ 0 = a
            for i in nums:
                ans = ans ^ i
            return ans


s = Solution()
lst = [4,1,2,1,2]
res1 = s.singleNumber1(lst)
res2 = s.singleNumber2(lst)
print(res1)
print(res2)