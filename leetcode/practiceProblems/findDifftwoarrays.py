answer = [[], []]
nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
h1 = {}
h2 = {}
for num in nums1:
    if num not in h1:
        h1[num] = 1
for num in nums2:
    if num not in h2:
        h2[num] = 1
for num in nums1:
    if num not in h2:
        if num not in answer[0]:
            answer[0].append(num)

for num in nums2:
    if num not in h1:
        if num not in answer[1]:
            answer[1].append(num)

print(answer)
