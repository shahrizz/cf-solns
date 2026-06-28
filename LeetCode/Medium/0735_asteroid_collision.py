asteroids = [3, 5, -6, 2, -1, 4]
stack = []

for asteroid in asteroids:
    while stack and stack[-1] > 0 and asteroid < 0:
        current = stack[-1]

        if abs(current) < abs(asteroid):
            stack.pop()
            continue

        elif abs(current) == abs(asteroid):
            stack.pop()
            break

        else:
            break
    else:
        stack.append(asteroid)

print(stack)
