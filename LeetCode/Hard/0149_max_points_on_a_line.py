points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
i = 0
ans = 0


def findSlope(point1: list, point2: list):
    if point1[0] == point2[0]:
        return float("inf")
    return (point1[1] - point2[1]) / (point1[0] - point2[0])


while i < len(points):
    anchor = points[i]
    h = {}
    j = 0
    while j < len(points):
        if j == i:
            j += 1
            continue
        slope = findSlope(anchor, points[j])
        if slope not in h:
            h[slope] = 1
        else:
            h[slope] += 1
        j += 1
    ans = max(ans, (max(h.values()) + 1))
    i += 1

print(ans)
