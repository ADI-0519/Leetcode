# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # traverse the 2 LL

        strA = ""
        strB = ""

        curr = l1
        while curr:
            strA += str(curr.val)
            curr = curr.next

        curr2 = l2
        while curr2:
            strB += str(curr2.val)
            curr2 = curr2.next

        strA = strA[::-1]
        strB = strB[::-1]


        sum = int(strA) + int(strB)
        sum_str = str(sum)

        head = None
        tail = None

        for i in range(len(sum_str)):
            if head == None:
                new_node = ListNode(int(sum_str[-(i+1)]))
                head = new_node
                tail = new_node
            else:
                new_node = ListNode(int(sum_str[-(i+1)]))
                tail.next = new_node
                tail = new_node

        return head


        

        