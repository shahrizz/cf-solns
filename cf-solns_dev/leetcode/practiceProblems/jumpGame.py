nums = [3, 2, 1, 0, 4]
furthest = 0

for i in range(len(nums)):
    if i > furthest:
        print(False)
        break

    furthest = max(furthest, i + nums[i])

print(True)
