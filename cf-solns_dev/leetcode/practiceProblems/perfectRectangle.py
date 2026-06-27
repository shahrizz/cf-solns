class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        corners = set()

        minX = float("inf")
        minY = float("inf")
        maxX = float("-inf")
        maxY = float("-inf")

        totalArea = 0

        for x1, y1, x2, y2 in rectangles:
            # Update bounding rectangle
            minX = min(minX, x1)
            minY = min(minY, y1)
            maxX = max(maxX, x2)
            maxY = max(maxY, y2)

            # Sum areas
            totalArea += (x2 - x1) * (y2 - y1)

            # Toggle the four corners
            for corner in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                if corner in corners:
                    corners.remove(corner)
                else:
                    corners.add(corner)

        # Area check
        if totalArea != (maxX - minX) * (maxY - minY):
            return False

        # Exactly four corners should remain
        expected = {
            (minX, minY),
            (minX, maxY),
            (maxX, minY),
            (maxX, maxY),
        }

        return corners == expected
