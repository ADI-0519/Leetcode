# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        tail = dummy
        
        cur = head.next # skip the head node
        rt = 0
        last_checkpoint = head 

        while cur:
            if cur.val != 0:
                rt += cur.val

            else:
                newnode = ListNode(rt)
                rt = 0
                tail.next = newnode
                tail = tail.next

                
            cur = cur.next
            

        

        return dummy.next

