from typing import List


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # first thought: binary search
        # used help for implementation details

        def compare_area(y, total_area):
            area_below = 0
            for sx, sy, sl in squares:
                if sy < y:
                    area_below += sl * min(y - sy, sl)
            return area_below >= total_area / 2

        def binsearch(h, l, total_area):
            # used help for defining the condition for diff
            while abs(h - l) > 1e-5:
                mid = (h + l) / 2
                if compare_area(mid, total_area):
                    # go lower
                    h = mid
                else:
                    # go higher
                    l = mid
            return h

        highest = 0
        total_area = 0
        for square in squares:
            total_area += square[2] ** 2
            highest = max(highest, square[1] + square[2])

        y = binsearch(highest, 0, total_area)

        return y
