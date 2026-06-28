grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
h = {}

i = 0
n = len(grid)
while i < n:
    j = 0
    temp = ""
    while j < n:
        temp = temp + str(grid[i][j])
        j += 1
    if temp not in h:
        h[temp] = 1
    else:
        h[temp] += 1
    i += 1

count = 0

j = 0
while j < n:
    i = 0
    temp = ""
    while i < n:
        temp += str(grid[i][j])
        i += 1

    if temp in h:
        count += h[temp]

    j += 1

print(count)
