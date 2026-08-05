"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        map = { None : None }


        point = head
        while point:
            copy = Node(point.val)
            map[point] = copy
            point = point.next


        point = head
        while point:
            copy = map[point]
            copy.next = map[point.next]
            copy.random = map[point.random]
            point = point.next

        return map[head]

        