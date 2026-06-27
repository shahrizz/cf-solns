height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
i = 0
j = len(height) - 1
totalWater = 0
left_max = 0
right_max = 0
total = 0
while i < j:
    if left_max < right_max:
        if height[i] < left_max:
            left_max = height[i]
        else:
            total += left_max - height[i]
        i += 1
    elif left_max > right_max:
        if height[j] < right_max:
            right_max = height[j]
        else:
            total += right_max - height[j]
        j -= 1
print(total)
