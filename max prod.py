nums = [1, 2, 3, 4]
nums.sort()
print(nums)
product1 = nums[-1] * nums[-2] * nums[-3]
product2 = nums[0] * nums[1] * nums[-1]
if product1 < product2:
    maximum = product2;
else:
    maximum = product2
print("maximum product:",maximum)
