nums = [8, 3, 0, 7, 2]
Sum = 0

for i in range(0, len(nums) - 1, 2): 
    Sum += nums[i] + nums[i + 1]

if len(nums) % 2 != 0:
    Sum += nums[-1]

print(Sum)
