from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # even number of negatives: they can all be removed
        # odd nubmer of negatives: can't remove all of them, so make the lowest magnitude cell negative
        nneg = 0
        s = 0
        smallest = None
        zeropresent = False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                av = abs(matrix[i][j])
                s += av
                if smallest == 0:
                    # smallest== 0 is carte blanche to make every num in matrix positive
                    # so just accrue the sum and skip counting negatives or updating smallest
                    continue
                if smallest is None:
                    smallest = av
                smallest = min(smallest, av)
                nneg += 1 if matrix[i][j] < 0 else 0
        print(f"smallest is {smallest}")
        if nneg % 2 == 0:
            # even num negatives
            return s
        else:
            assert isinstance(smallest, int)
            return s - 2*smallest