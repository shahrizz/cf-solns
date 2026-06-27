def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # choose middle element as pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


mass = 10
asteroids = [3, 9, 19, 5, 21]
asteroids = quick_sort(asteroids)
i = 0
for asteroid in asteroids:
    if mass >= asteroid:
        mass += asteroid
        i += 1
    else:
        break

if i == len(asteroids):
    print(True)
else:
    print(False)
