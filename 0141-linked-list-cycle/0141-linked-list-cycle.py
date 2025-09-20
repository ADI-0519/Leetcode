# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        hashset = set()
        cur = head

        while cur:
            if cur not in hashset:
                hashset.add(cur)
            else:
                return True
            cur = cur.next

        return False