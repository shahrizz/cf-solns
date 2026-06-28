nums = [2, 5, 6, 0, 0, 1, 2]
target = 1
left = 0
right = len(nums) - 1

while left <= right:
    mid = (left+right) // 2

    if nums[mid] == target:
        print(True)
        break
s
    # duplicates?
    # if ...:
    #     ...

    # left half sorted?
    elif nums[left] <= nums[mid]:
        if target is inside [nums[left], nums[mid]):
            ...
        else:
            ...

    # otherwise right half sorted
    else:
        if target is inside (nums[mid], nums[right]]:
            ...
        else:
            ...
