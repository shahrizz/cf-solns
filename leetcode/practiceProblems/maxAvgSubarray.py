nums = [1, 12, -5, -6, 50, 3]
k = 4
i = 0
j = i + k
maxAvg = 0
while j < len(nums):
    maxAvg = max(maxAvg, (sum(nums[i:j])) / k)
    i += 1
    j += 1
print(maxAvg)
