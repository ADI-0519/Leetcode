# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = None
        p2 = head

        while p2:
            next_node = p2.next
            p2.next = p1
            p1 = p2
            head = p2
            p2 = next_node
            
        

        
        return head
            
            

            

