# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        fast = head
        slow = head
        

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        # slow points to the start of second list we need to splice


        # reverse second half

        p1,p2 = None,slow.next
        slow.next = None
        head2 = None

        while p2:
            head2 = p2
            temp = p2.next
            p2.next = p1

            p1 = p2
            p2 = temp

        p1 = head
        p2 = head2
        

        while p1 and p2:
            temp = p1.next
            p1.next = p2
            temp2 = p2.next
            p2.next = temp

            p1 = temp
            p2 = temp2
        
        return head



