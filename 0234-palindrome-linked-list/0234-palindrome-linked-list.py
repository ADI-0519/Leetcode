# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        p1 = head
        arr = []
        while p1:
            arr.append(p1.val)
            p1 = p1.next

        low,high = 0, len(arr)-1
        while low<=high:
            if arr[low] == arr[high]:
                low += 1
                high -= 1
            else:
                return False

        return True