# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        self.total = 0
        def dfs(node):
            if node is None:
                return 0
            if node.val >= low and node.val <= high:
                self.total += node.val
            if node.left and node.val > low:
                dfs(node.left)
            if node.right and node.val < high:
                dfs(node.right)
        dfs(root)
        return self.total