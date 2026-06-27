nums = [1,7,3,6,5,6]

total = sum(nums)
leftSum = 0
output = -1
for i in range(len(nums)):
    rightSum = total - leftSum - nums[i]

    if leftSum == rightSum:
        output = i
        break

    leftSum += nums[i]