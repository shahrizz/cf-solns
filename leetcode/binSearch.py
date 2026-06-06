left = 0
right = len(nums) - 1
ans = -1
while left < right:
    mid = (left + right) // 2
    if nums[mid] == target:
        ans = mid
        break
    elif nums[mid] < target:
        left = mid + 1
    elif nums[mid] > target:
        right = mid - 1

print(ans)
