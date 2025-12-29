# had to look at solutions for this one but I added the comments to explain

from collections import defaultdict
from itertools import pairwise, product
from typing import Dict, List, Tuple


class Solution:
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
        # define a transition map which gives top block given bottom left and right
        tmap: Dict[Tuple[str, str], List[str]] = defaultdict(list)
        for a, b, c in allowed:
            tmap[a, b].append(c)

        # try to build one layer of pyramid (recursion)
        def can_build_pyramid(layer: str | list[str]) -> bool:
            if len(layer) == 1:
                # already solved
                return True
            else:
                # check all possible iterations of the layer above this one
                # return true if one of them is valid
                return any(
                    map(
                        can_build_pyramid,
                        product(*(tmap[a, b] for a, b in pairwise(layer))),
                    )
                )

        # first instance of the recursion
        return can_build_pyramid(bottom)
