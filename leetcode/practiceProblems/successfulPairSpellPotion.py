spells = [5, 1, 3]
potions = [1, 2, 3, 4, 5]
potions.sort()
success = 7
answer = []
for spell in spells:
    left = 0
    right = len(potions) - 1

    while left <= right:
        mid = (left + right) // 2

        if spell * potions[mid] < success:
            left = mid + 1
        else:
            right = mid - 1

    answer.append(len(potions) - left)

print(answer)
