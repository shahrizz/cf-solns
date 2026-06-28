nums = [2, 2, 1, 1, 1, 2, 2]
h = {}
for num in nums:
    h[num] = h.get(num, 0) + 1
# print(h)
max_freq = 0
max_num = None

for num, count in h.items():
    if count > max_freq:
        max_freq = count
        max_num = num
print(max_num)
