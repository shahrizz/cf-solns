nums = [1, 2, 3, 4, 1]

for i in range(len(nums)):
    k = i
    while k <= len(nums):
        print(k)
        if nums[i] == nums[k]:
            print(True)
            break
        else:
            continue
        