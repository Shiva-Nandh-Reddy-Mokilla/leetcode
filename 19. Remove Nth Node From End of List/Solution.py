# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        prev=None
        current=head
        h=head
        countfromfront=0
        countsecond=0
        while current:
            current=current.next
            countfromfront+=1
        target=countfromfront-n
        position=0
        current=head
        if target==0:
            return head.next
        while current:
            position+=1
            
            if position==target:
                current.next=current.next.next if current.next else None
            current=current.next
            
        return head
            
        
            
            
        
            
       

        