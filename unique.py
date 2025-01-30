nums = [1, 2, 3, 3, 3, 3, 4, 5]
nums2 = []

for i in range(len(nums) - 1):
    if nums[i] != nums[i + 1]:
        nums2.append(nums[i])

nums2.append(nums[-1])

print(nums2)
