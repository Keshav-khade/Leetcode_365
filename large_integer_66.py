# nums = [1,2,3]
# nums = []
# nums = [1]
# nums = [0]
# nums = [9,9,9]
nums = [1,9,9]

if len(nums) == 0:
    print("empty")
carry = 1
i = len(nums) - 1
while i >= 0:
    digit = nums[i] + carry
    remainder = digit % 10
    carry = digit // 10
    nums[i] = remainder
    if carry == 0:
        break
    i -= 1
if carry == 1:
    nums.insert(0,carry)

print(nums)