# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h = l1
        h2 = l2
        n1 = ""
        n2 = ""
        
        # Extract digits in reverse order
        while h:
            n1 += str(h.val)
            h = h.next
        while h2:
            n2 += str(h2.val)
            h2 = h2.next
        
        # Reverse strings to get correct number
        number = int(n1[::-1]) + int(n2[::-1])
        
        # Convert the result back to reversed list of digits
        digits = list(str(number))[::-1]

        # Build the resulting linked list
        dummy = ListNode(0)
        current = dummy
        for digit in digits:
            current.next = ListNode(int(digit))
            current = current.next

        return dummy.next
