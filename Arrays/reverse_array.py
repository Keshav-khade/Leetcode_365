"""
# reverse the array using slicing

nums = [1, 2, 3, 4, 5]
nums = [1, 2]
nums = [1]
nums = []

nums1 = nums[-1::-1]
nums2 = nums[::-1]
print(nums1)
print(nums2)

"""

"""
# nums = [1, 2, 2, 3, 4]
# nums = [5, 5, 5, 5]
# nums = [-1, -2, -3, -4]	
nums = [-5, 2, -1, 8, 0]

# using two pointer and swapping approach
left = 0
right = len(nums) -1

while left <= right:
          temp = nums[left]
          nums[left] = nums[right]
          nums[right] = temp

          # you can replace the above logic with this
          nums[left], nums[right] = nums[right], nums[left]

          left += 1
          right -= 1

print(nums)
"""