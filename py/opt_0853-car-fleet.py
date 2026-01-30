from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort by position
        road = list(zip(position, speed))
        road.sort(key=lambda x: x[0])

        # get arrival times for each car
        road = [(target - pos) / sp for pos, sp in road]

        # car cannot arrive before car in front of it
        for i in range(len(road) - 2, -1, -1):
            if road[i + 1] > road[i]:
                road[i] = road[i + 1]

        # count unique arrival times
        return len(set(road))
