nums = [4, 5, 6, 7, 0, 1, 2]
left = 0
right = len(nums) - 1
while left < right:
    mid = (left + right) // 2
    if nums[mid] > nums[right]:
        left = mid + 1
    else:
        right = mid - 1

print(nums[left])
