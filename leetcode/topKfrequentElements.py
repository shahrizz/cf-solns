nums = [
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,  # 10
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,  # 9
    3,
    3,
    3,
    3,
    3,
    3,
    3,
    3,  # 8
    4,
    4,
    4,
    4,
    4,
    4,
    4,  # 7
    5,
    5,
    5,
    5,
    5,
    5,  # 6
    6,
    6,
    6,
    6,
    6,  # 5
    7,
    7,
    7,
    7,  # 4
    8,
    8,
    8,  # 3
    9,
    9,  # 2
    10,  # 1
]

k = 5
n = len(nums)
freq = {}


for num in nums:
    if num not in freq:
        freq[num] = 1
    elif num in freq:
        freq[num] += 1

updated = list(freq.items())
i = 0
bucket = [[] for _ in range(len(nums) + 1)]
while i < len(updated):
    num = updated[i][0]
    count = updated[i][1]
    bucket[count].append(num)
    i += 1

res = []
for frequency in range(len(bucket) - 1, 0, -1):
    for num in bucket[frequency]:
        res.append(num)
        if len(res) == k:
            break
    if len(res) == k:
        break

return res
