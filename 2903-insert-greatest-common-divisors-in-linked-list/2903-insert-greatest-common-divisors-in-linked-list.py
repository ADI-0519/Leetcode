# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = head
        p2 = head.next

        def Hcf(x,y):
            while(y):
                x, y = y, x % y
            return x

        while p1.next != None:
            hcf = Hcf(p1.val,p2.val)
            hcf_node = ListNode(hcf,p2)
            p1.next = hcf_node
            p2 = hcf_node.next.next
            p1 = hcf_node.next

        return head

            