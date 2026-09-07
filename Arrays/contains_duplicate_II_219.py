"""
lc - 219
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
"""

# nums = [1,2,3,1]
# nums = [1,2,3,1,2,3]
nums = [1,0,1,1]
# k = 3
# k = 2
k = 1

"""
@-TLE
n = len(nums)
flag = False
for i in range(n):
    for j in range(i+1,n):
        if nums[i] == nums[j]:
            if abs(i-j) <= k:
                flag = True
                print("True")
                break
        if flag:
            break
if not flag:
    print("False")
"""

"""

"""
nums = [1,0,1,1]
k = 1

# nums = [1,2,3,1]
# k = 3

"""
# better approach with hashmap logic

d = {}
n = len(nums)
flag = False
for i in range(n):
    if nums[i] in d:
        if abs(i - d.get(nums[i],0)) <= k:
            flag = True
            print("True")
            break
    d[nums[i]] = i

if not flag:
    print("False")
"""


# final approach for this question sliding window
nums = [1,2,3,1]
k = 3

# nums = [1,0,1,1]
# k = 1

# nums = [1,2,3,1,2,3]
# k = 2

def duplicate2(nums,k):
    j = 0
    seen = set()
    for i in range(len(nums)):
        if nums[i] in seen:
                return True
        seen.add(nums[i])
        if len(seen) > k:
            seen.remove(nums[j])
            j += 1
    return False

res = duplicate2(nums,k)
print(res)


