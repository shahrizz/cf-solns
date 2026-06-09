arr = [2, 3, 4, 5, 5, 12, 14]
target = 5
left = 0
right = len(arr) - 1
ans = 0

while left <= right:
    mid = (left + right) // 2

    if arr[mid] <= target:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)