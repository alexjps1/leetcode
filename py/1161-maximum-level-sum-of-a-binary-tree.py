from collections import defaultdict
from typing import Optional, List, Tuple, Dict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# intuition: record the effect that each node has on the sum
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue: List[Tuple[TreeNode, int]] = [(root,  1)]
        d: Dict[int, int] = defaultdict(int)
        while len(queue):
            # bfs (dfs would also work just fine)
            cur, lvl = queue.pop(0)
            d[lvl] += cur.val
            if cur.left:
                queue.append((cur.left, lvl+1))
            if cur.right:
                queue.append((cur.right, lvl+1))
        maxval: int | None = None
        ans: int = 0
        for i in d.keys():
            if maxval is None or d[i] > maxval:
                maxval = d[i]
                ans = i
        return ans


        
