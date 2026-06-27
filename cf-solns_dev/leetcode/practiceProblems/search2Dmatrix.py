matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
# # m = len(matrix)  rows
# # n = len(matrix[0])  columns
# left_i = 0
# left_j = 0
# right_i = len(matrix) - 1
# right_j = len(matrix[0]) - 1
# while left_i < right_i and left_j < right_j:
#     mid_i = ((left_i) + (right_i)) // 2
#     mid_j = ((left_j) + (right_j)) // 2
#     if matrix[mid_i][mid_j] > target:
#         right_i = mid_i - 1
#         right_j = mid_j - 1
#     else:
#         left_i = mid_i + 1
#         left_j = mid_j + 1
# print(left_i)
# print(left_j)

m = len(matrix)
n = len(matrix[0])

left = 0
right = m * n - 1

while left <= right:
    mid = (left + right) // 2

    row = mid // n
    col = mid % n

    if matrix[row][col] == target:
        print(True)
        break
    elif matrix[row][col] < target:
        left = mid + 1
    else:
        right = mid - 1
else:
    print(False)
