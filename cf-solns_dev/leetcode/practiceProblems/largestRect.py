heights = [2, 1, 5, 6, 2, 3]
i = 0
j = 0
maxArea = 0
while i < len(heights) and j < len(heights):
    if heights[i] < heights[j]:
        i += 1
