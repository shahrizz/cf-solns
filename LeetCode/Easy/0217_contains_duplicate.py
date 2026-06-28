nums = [1, 2, 3, 1]
h = {}

for num in nums:
    if num in h:
        print(True)
    else:
        h[num] = 1
