height = [1,8,6,2,5,4,8,3,7]

maxArea = 0
currArea = 0
# while i < len(height):
#     print('first loop')
#     j = len(height) - 1
#     while j > i:
#         print("second loop")
#         breath = abs(j - i)
#         h = min(height[i], height[j])
#         currArea = breath * h
#         if currArea >= maxArea:
#             maxArea = currArea

i = 0
j = len(height) - 1
while i != j:
    currArea = (abs(j - i))*(min(height[i], height[j]))
    if currArea >= maxArea:
        maxArea = currArea
    if height[i] < height[j]:
        i = i + 1
    else:
        j = j - 1

print(maxArea)