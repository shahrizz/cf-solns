nums = [2, 2, 3, 1, 4, 5, 4, 2, 1, 3, 2]
h = set()
for num in nums:
    h.add(num)

h = list(h)
h.sort()
if len(h) >= 3:
    print(h[-3])
else:
    print(h[-1])
