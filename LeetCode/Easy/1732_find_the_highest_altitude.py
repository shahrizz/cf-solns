gain = [-5, 1, 5, 0, -7]
prefix_gain = []
sum = 0
i = 0
while i < len(gain):
    sum += gain[i]
    prefix_gain.append(sum)
    i += 1

maxHeight = 0
print(max(maxHeight, max(prefix_gain)))
