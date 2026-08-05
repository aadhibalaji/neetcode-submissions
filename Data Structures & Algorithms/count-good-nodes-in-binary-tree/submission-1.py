# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        res = 0
        def dfs(curr, greatest, res):
            if not curr:
                return res

            if curr.val >= greatest:
                res += 1
            
            res = dfs(curr.left, max(curr.val, greatest), res)
            res = dfs(curr.right, max(curr.val, greatest), res)

            return res
    
        return dfs(root, root.val, res)


            

        