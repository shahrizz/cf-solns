nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
h = set()
for i in range(0, len(nums) + 1):
    h.add(i)
for num in nums:
    if num in h:
        h.remove(num)
answer = h.pop()
print(answer)
