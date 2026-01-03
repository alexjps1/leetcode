from collections import defaultdict
from typing import Dict, List, Tuple


# coded with minimal hints and did not look at editorial, took 1h+ :/
class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7

        def check_coloring(prevtype: int, newtype: int):
            # assume prev is valid
            prev = rowtypes[prevtype]
            new = rowtypes[newtype]
            for i in range(3):
                if prev[i] == new[i]:
                    return False
            if new[0] == new[1] or new[1] == new[2]:
                return False
            return True

        def find_next_perms(prevtype: int):
            return [check_coloring(prevtype, candidate) for candidate in range(12)]

        # permutations
        rowtypes: List[Tuple[int, int, int]] = [
            # 2 color
            (1, 2, 1),
            (2, 1, 2),
            (1, 3, 1),
            (3, 1, 3),
            (2, 3, 2),
            (3, 2, 3),
            # 3 color
            (1, 2, 3),
            (1, 3, 2),
            (2, 1, 3),
            (2, 3, 1),
            (3, 1, 2),
            (3, 2, 1),
        ]

        # ways to get to each permutation in each row
        dp: Dict[int, Dict[int, int]] = {0: {i: 1 for i in range(12)}}

        cachednextperms: Dict[int, List[bool]] = {}

        for row in range(n):
            # update dp to the next row
            dp[row + 1] = defaultdict(int)
            for p in range(12):
                if dp[row][p] == 0:
                    continue
                else:
                    trycache = cachednextperms.get(p)
                    if trycache is not None:
                        next_perms = trycache
                    else:
                        next_perms = find_next_perms(p)
                        cachednextperms[p] = next_perms
                    for i in range(12):
                        if next_perms[i]:
                            dp[row + 1][i] = (dp[row + 1][i] + dp[row][p]) % MOD

        return sum(dp[n - 1][i] for i in range(12)) % MOD


# first attempt (wrong approach, did not pass non-trivial test cases)
"""
class Solution:
    def numOfWays(self, n: int) -> int:

        rowtypes: List[Tuple[int, int, int]] = [
            # 2 color
            (1, 2, 1), (2, 1, 2), (1, 3, 1), (3, 1, 3), (2, 3, 2), (3, 2, 3),
            # 3 color
            (1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)
        ]

        # answer, tells number of combinations possible for row n
        w: Dict[int, int] = {
            0: 12
        }

        # rowtypes that are possible at row i
        possible: Dict[int, List[bool]] = {
            0: [True] * 12
        }

        # dp array, tells which rowtypes can follow a particular rowtype
        maprowtypes: Dict[int, List[int]] = {}

        # dp array, maps possible[n] to possible[n+1] if already known
        # (not strictly necessary)
        mappossible: Dict[str, List[bool]] = {}

        def hlist(l):
            return "".join("t" if i else "f" for i in l)

        def check_coloring(prevtype: int, newtype: int):
            # assume prev is valid
            prev = rowtypes[prevtype]
            new = rowtypes[newtype]
            for i in range(3):
                if prev[i] == new[i]:
                    return False
            if new[0] == new[1] or new[1] == new[2]:
                    return False
            return True

        def find_acceptable_colorings(prevtype: int):
            return [check_coloring(prevtype, candidate) for candidate in range(12)]

        def or_lists(l1, l2):
            return [a or b for a, b in zip(l1, l2)]

        def iterpossible(row):
             # give possible[n+1] based on possible[n]
            trycache = mappossible.get(hlist(possible[row]))
            if trycache is not None:
                return trycache

            nextpossible = [False] * 12
            for i in range(12):
                # find nextpossible rowtypes given current possible rowtypes
                if possible[row][i] == False:
                    continue
                trycache = maprowtypes.get(i)
                if trycache is not None:
                    nextpossible = or_lists(nextpossible, trycache)
                else:
                    acceptable_colorings = find_acceptable_colorings(i)
                    nextpossible = or_lists(nextpossible, acceptable_colorings)
                    # cache for next time
                    maprowtypes[i] = acceptable_colorings

            # cache for next time
            mappossible[hlist(possible[row])] = nextpossible

            return nextpossible

        for i in range(n-1):
            possible[i+1] = iterpossible(i)
            w[i+1] = w[i] + possible[i+1].count(True)

        print(w)
        print(possible)

        return w[n-1]
"""
