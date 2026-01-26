from typing import List

# my first (non-optimal) solution


class FirstSolution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def valid_set(lst: list):
            nums = [item for item in lst if item != "."]
            return len(set(nums)) == len(nums)

        valid = True

        # rows
        for row in board:
            valid = min(valid, valid_set(row))
            if not valid:
                print(f"invalidated at row {row}")

        # cols
        for i in range(9):
            col = [board[j][i] for j in range(9)]
            valid = min(valid, valid_set(col))
            if not valid:
                print(f"invalidated at col{i}")
                print(f"col contents: {col}")

        # boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = []
                square += board[i][j : j + 3]
                square += board[i + 1][j : j + 3]
                square += board[i + 2][j : j + 3]
                valid = min(valid, valid_set(square))
                if not valid:
                    print(f"invalidated at square {i},{j}")
                    print("square contents: ", square)

        return valid


# optimal solution
# I read that I had to use a bitmasks but made my own implementation


class OptimalSolution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for i in range(9):  # row
            for j in range(9):  # col
                val = board[i][j]
                if val == ".":
                    continue
                k = 3 * (i // 3) + j // 3  # square
                print(i, j, k)
                bit = 1 << (int(val) - 1)
                if (rows[i] | cols[j] | squares[k]) & bit > 0:
                    return False
                rows[i] |= bit
                cols[j] |= bit
                squares[k] |= bit

        return True
