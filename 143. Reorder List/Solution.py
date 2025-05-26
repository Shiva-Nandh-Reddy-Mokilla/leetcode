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
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next


        prev=None
        current=slow.next
        slow.next=None
        while current:
            nex=current.next
            current.next=prev
            prev=current
            current=nex
        h=ListNode(0)
        count=1
      

        while h and prev:
            if count&1:
                h.next=head
                h=h.next
                head=head.next
            else:
                h.next=prev
                h=h.next
                prev=prev.next
            count+=1
        if prev:
            h.next=prev
        if head:
            h.next=head



            
            

            
        

        

        

        

        