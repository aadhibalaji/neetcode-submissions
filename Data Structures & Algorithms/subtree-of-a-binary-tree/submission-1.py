# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(curr, sub):
            if not curr and not sub:
                return True
            if not sub or not curr:
                return False
            
            if curr.val != sub.val:
                return False
            
            left = dfs(curr.left, sub.left)
            right = dfs(curr.right, sub.right)

            return True if left and right else False
        
        if not root:
            return False

        res = dfs(root, subRoot)

        if res:
            return True
        
        

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        