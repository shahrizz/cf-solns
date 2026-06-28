nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
i = 0

h = set()
while i < len(nums):
    if nums[i] not in h:
        h.add(nums[i])
        i += 1
    else:
        nums.pop(nums[i])
print(nums)
