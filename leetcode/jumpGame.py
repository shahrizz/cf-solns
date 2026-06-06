nums = [2, 3, 1, 1, 4]
furthest = 0
first = 0
last = len(nums) - 1
i = 0
while True:
    if i >= last:
        print(True)
        break
    elif i >= furthest:
        furthest = i
    i += nums[i]
