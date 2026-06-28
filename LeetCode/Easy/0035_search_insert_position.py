nums = [1, 3, 5, 6]
target = 7
first = 0
last = len(nums) - 1
if target >= nums[len(nums) - 1]:
    print(len(nums))
while first <= last:
    mid = (first + last) // 2
    if nums[mid] == target:
        print(mid)
        break
    if nums[mid] < target:
        first = mid + 1
    if nums[mid] > target:
        last = mid - 1
    if first == last:
        print(mid)
        break
