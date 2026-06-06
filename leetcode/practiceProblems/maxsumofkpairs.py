nums = [1, 2, 3, 4]
k = 5   
complement = []
for i in range(len(nums)):
    complement.append(abs(nums[i] - k))

i = 0
j = 1
k = 0
while i < len(nums):
    while j < len(complement):
        if nums[i] == complement[j]:
            k = k + 1
            nums.pop(i)
        j = j + 1

    i = i + 1

print(k)