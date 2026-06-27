arr = [1, 2, 2, 1, 1, 3]
h = {}
for element in arr:
    if element in h:
        h[element] += 1
    else:
        h[element] = 1

freqs = list(h.values())
k = {}
for freq in freqs:
    if freq not in k:
        k[freq] = 1
    else:
        break
