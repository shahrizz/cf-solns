nums = [0]
i = 0
j = len(nums)
while i < j:
    if nums[i] == 0:
        nums.append(0)
        nums.pop(i)
    i += 1
print(nums)
