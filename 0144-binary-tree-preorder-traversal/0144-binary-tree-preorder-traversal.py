# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stk = [root]
        arr = []

        if root == None:
            return arr

        while stk:
            node = stk.pop()
            arr.append(node.val)
            if node.right:
                stk.append(node.right)
            if node.left:
                stk.append(node.left)

        return arr