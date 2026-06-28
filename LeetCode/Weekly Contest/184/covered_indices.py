# from heapq import heappop, heappush

# nums = [11, 11, 14, 10]
# s = "1011"
# final = [int(s[_]) for _ in range(len(nums))]
# i = 1
# while i < len(nums):
#     if final[i] == 1:
#         if max(nums[i], nums[i - 1]) == nums[i - 1]:
#             temp = final[i - 1]
#             final[i - 1] = final[i]
#             final[i] = temp
#     i += 1

# finalSum = 0
# for i in range(len(nums)):
#     if final[i] == 1:
#         finalSum += nums[i]

# print(finalSum)

# heap = []
# ans = 0

# for i in range(len(nums)):
#     if s[i] == "1":
#         heappush(heap, nums[i])

#     if heap and nums[i] > heap[0]:
#         ans += nums[i]
#         heappush(heap, nums[i])
#         heappop(heap)

# print(ans)


nums = [9, 2, 6, 1]
s = "0101"
n = len(nums)
if n == 0:
    print(0)

if s[0] == "1":
    a = nums[0]
    b = nums[0]
else:
    a = 0
    b = nums[0]

i = 1
while i < n:
    if s[i] == "1":
        new_a = max(nums[i] + a, b)

        new_b = max(nums[i] + a, nums[i] + b)
    else:
        new_a = a
        new_b = nums[i] + a

    a, b = new_a, new_b
    i += 1


print(a)
