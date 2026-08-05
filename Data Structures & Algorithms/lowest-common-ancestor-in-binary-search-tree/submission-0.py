# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        #need to search for both nodes, keep track of the smallest ancestor

        def dfs(curr):
            
            if curr.val > p.val and curr.val > q.val:
                return dfs(curr.left)
            if curr.val < p.val and curr.val < q.val:
                return dfs(curr.right)
            else:
                return curr


        return dfs(root) 
            
