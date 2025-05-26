class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Step 1: Find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        prev = None
        current = slow.next
        slow.next = None
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        # Step 3: Merge using count toggle
        first, second = head, prev
        dummy = ListNode(0)
        tail = dummy
        count = 0

        while first and second:
            if count % 2 == 0:
                tail.next = first
                first = first.next
            else:
                tail.next = second
                second = second.next
            tail = tail.next
            count += 1

        # Append remaining node (if any)
        tail.next = first or second
