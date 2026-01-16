from typing import List


# used editorial to prove and refine existing intuition
class Solution:
    def maximizeSquareArea(
        self, m: int, n: int, hBars: List[int], vBars: List[int]
    ) -> int:
        MOD = 10**9 + 7

        hBars = [1] + hBars + [m]
        vBars = [1] + vBars + [n]

        hset = set()
        for i in hBars:
            for j in hBars:
                hset.add(i - j)

        vset = set()
        for i in vBars:
            for j in vBars:
                vset.add(i - j)

        for i in sorted(list(hset), reverse=True):
            if i == 0:
                return -1
            if i in vset:
                return int(i**2 % MOD)
        return -1
