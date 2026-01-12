class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:

        def point_to_point(p1: tuple[int, int], p2: tuple[int, int]):
            # effectively the chebyshev distance
            xdiff = abs(p1[0] - p2[0])
            ydiff = abs(p1[1] - p2[1])
            return max(xdiff, ydiff)

        return sum(point_to_point(points[i], points[i+1]) for i in range(len(points) - 1))
