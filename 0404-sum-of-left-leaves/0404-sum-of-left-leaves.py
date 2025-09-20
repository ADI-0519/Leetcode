# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        stk = [root]
        total = 0

        while stk:
            node = stk.pop()
            if node.left:
                stk.append(node.left)
                
                if node.left.left == None and node.left.right == None:
                    total += node.left.val

            if node.right:
                stk.append(node.right)


        return total