# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# sick day,  worked out pseudocode by hand but used an online solution and commented it
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7

        def dfs(node):
            if not node:
                return 0

            # edit node vals to contain subtree sum
            node.val += dfs(node.left) + dfs(node.right)
            return node.val

        # simultaneously store subtree sums in all nodes and get total sum of all nodes
        total = dfs(root)

        ans = 0
        q = deque([root])

        while q:
            node = q.popleft()
            if not node:
                continue

            # maximize product
            current_product = (total - node.val) * node.val
            ans = max(ans, current_product)

            # traverse all nodes to consider all splittings
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return ans % MOD
