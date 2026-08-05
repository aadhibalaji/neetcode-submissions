# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        
        def dfs(curr):
            if not curr:
                return 0

            right = dfs(curr.right)
            left = dfs(curr.left)

            if left == -1 or right == -1:
                return -1
            
            if abs(left - right) > 1:
                return -1

            return 1 + max(dfs(curr.left), dfs(curr.right))

        

        res = dfs(root)

        if res == -1:
            return False
        else:
            return True