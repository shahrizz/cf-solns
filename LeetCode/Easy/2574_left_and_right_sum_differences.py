nums = [1]
leftSum = [0]
leftsumval = 0
rightsumval = sum(nums) - nums[0]
rightSum = [rightsumval]
computed = []
i = 1
while i < (len(nums)):
    leftsumval += nums[i - 1]
    rightsumval -= nums[i]
    leftSum.append(leftsumval)
    rightSum.append(rightsumval)
    i += 1

for i in range(len(leftSum)):
    computed.append(abs(leftSum[i] - rightSum[i]))

print(computed)
