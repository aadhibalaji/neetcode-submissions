# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        stack = []

        pointer = head.next

        while pointer:
            stack.append(pointer)

            pointer = pointer.next

        pointer = head
        counter = 0
        for i in range(len(stack)):
            if counter % 2 == 0:
                pointer.next = stack.pop()
            else:
                pointer.next = stack.pop(0)
            pointer = pointer.next
            counter += 1
        
        pointer.next = None
        
