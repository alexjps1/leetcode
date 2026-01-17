from typing import List


# simple brute force approach
class Solution:
    def largestSquareArea(
        self, bottomLeft: List[List[int]], topRight: List[List[int]]
    ) -> int:
        def intersection(bl1, tr1, bl2, tr2):
            if bl1 == bl2 and tr1 == tr2:
                return 0
            # i used help to write this helper function
            x1, y1 = bl1
            x2, y2 = tr1
            x3, y3 = bl2
            x4, y4 = tr2
            x5 = max(x1, x3)
            y5 = max(y1, y3)
            x6 = min(x2, x4)
            y6 = min(y2, y4)
            if x5 > x6 or y5 > y6:
                return 0
            min_length = min(x6 - x5, y6 - y5)
            return min_length**2

        largest_area = 0
        for i in range(len(bottomLeft)):
            for j in range(len(bottomLeft)):
                largest_area = max(
                    largest_area,
                    intersection(
                        bottomLeft[i], topRight[i], bottomLeft[j], topRight[j]
                    ),
                )

        return largest_area
