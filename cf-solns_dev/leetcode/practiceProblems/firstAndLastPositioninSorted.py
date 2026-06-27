nums = [5, 7, 7, 8, 8, 10]
target = 8
left = 0
right = len(nums) - 1
ans = []
while left < right:
    mid = (left + right) // 2
    if nums[left] == nums[right]:
        print(left)
        print(right)
        break
    if nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
