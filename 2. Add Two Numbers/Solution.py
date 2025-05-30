# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        sumof=0
        dummy=ListNode()
        res=dummy
        while l1 or l2 or carry:
            sum=carry
            if l1:
                sum+=l1.val
                l1=l1.next 
            if l2:
                sum+=l2.val
                l2=l2.next
           
            carry=sum//10
            dummy.next=ListNode(sum%10)
            dummy=dummy.next
          
        return res.next

        



            
        