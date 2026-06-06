# gas = [2, 3, 4]
# cost = [3, 4, 3]
# tank = 0
# stIndex = -1
# j = 0
# while j < len(gas):
#     i = j
#     tank = 0
#     while i != stIndex:
#         if tank < 0:
#             stIndex = j
#             break

#         if i >= len(gas):
#             i = 0
#         else:
#             tank += gas[i] - cost[i]

#         i += 1
#     j += 1

# print(stIndex - 1)
gas = [2, 3, 4]
cost = [3, 4, 3]

n = len(gas)

for start in range(n):
    tank = 0
    success = True

    for step in range(n):
        i = (start + step) % n

        tank += gas[i] - cost[i]

        if tank < 0:
            success = False
            break

    if success:
        print(start)
        break
else:
    print(-1)
