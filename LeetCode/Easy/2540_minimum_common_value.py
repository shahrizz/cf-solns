nums1 = [1, 2, 3]
nums2 = [2, 4]

i = 0
j = 0
while i < len(nums1) and j < len(nums2):
    if nums1[i] in nums2:
        print(nums1[i])
        break
    i += 1
    j += 1
