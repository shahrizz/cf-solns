descriptions = [[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]]
# [50,20,80,15,17,19]
h = {}
for i in range(len(descriptions)):
    for value in descriptions[i]:
        if value not in h:
            h[value] = 1
print(h)
