nums = [3, 1, 2, 5, 6, 4]
preProd = []
postProd = []
i = 0
j = len(nums) - 1
l1 = 1
l2 = 1
while i < len(nums) and j >= 0:
    preProd.append(l1)
    l1 *= nums[i]
    postProd.append(l2)
    l2 *= nums[j]
    i += 1
    j -= 1
m = 0
n = len(postProd) - 1
final = []
while m < len(preProd) and n >= 0:
    final.append((preProd[m]) * (postProd[n]))
    m += 1
    n -= 1
print(final)
