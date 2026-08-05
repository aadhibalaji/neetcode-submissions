# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        tree = []
        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = collections.deque()

            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                tree.append(level)

        res = []
        for i in range(len(tree)):
            res.append(tree[i].pop().val)

        return res
    
            