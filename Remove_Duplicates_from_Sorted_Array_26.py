# this is question 26.
"""
1. [] , () , {} ,"" -> empty containers by default python treat as false
2. is -> keyword is useful for check identity or objects, like [] is [] is these objects are pointing to the same object in the memory.
"""

def remove_duplicate(nums):
        i = 0
        for j in range(1,len(nums)):
                if nums[i] != nums[j]:
                        nums[i+1] = nums[j]
                        i += 1
        return i+1               

arr = [0,0,1,1,1,2,2,3,3,4]
res = remove_duplicate(arr)
print(res)