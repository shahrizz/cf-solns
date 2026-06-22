costs = [1, 3, 2, 4, 1]
coins = 7
mx = max(costs)

freq = [0] * (mx + 1)

for x in costs:
    freq[x] += 1

prefixSum = []
s = 0

for value in freq:
    s += value
    prefixSum.append(s)

prefixSum.insert(0, 0)
prefixSum.pop()

costs_sorted = [0] * len(costs)

for i in range(len(freq)):
    while freq[i] > 0:
        costs_sorted[prefixSum[i]] = i
        prefixSum[i] += 1
        freq[i] -= 1

number = 0
for iceCream in costs_sorted:
    if coins <= 0:
        break
    coins -= iceCream
    number += 1
