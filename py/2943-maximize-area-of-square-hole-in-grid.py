from typing import List


class Solution:
    def maximizeSquareHoleArea(
        self, n: int, m: int, hBars: List[int], vBars: List[int]
    ) -> int:
        # just find the longest horizontal and longest vertical gap
        # then return the shorter of the two
        def max_gap(bars):
            if len(bars) == 0:
                return 1
            max_gap = 2
            curgap = 2
            for i in range(1, len(bars)):
                if bars[i - 1] == bars[i] - 1:
                    curgap += 1
                else:
                    curgap = 2
                max_gap = max(max_gap, curgap)
            return max_gap

        h = max_gap(sorted(hBars))
        v = max_gap(sorted(vBars))
        print(f"h is {h} and v is {v}")

        return min(h, v) ** 2
