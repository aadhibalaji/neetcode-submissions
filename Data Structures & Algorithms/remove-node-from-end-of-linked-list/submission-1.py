# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
        
        length = 0
        point = head

        while point:
            length += 1
            point = point.next

        index = length - n
        point = head
        
        if (index == 0):
            return head.next

        for i in range(index):
            temp = point
            point = point.next

        temp.next = point.next

        return head