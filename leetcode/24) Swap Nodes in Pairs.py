class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first=head
        while head and head.next:
            current=head
            nextt=current.next
            current.val , nextt.val=nextt.val, current.val
            head=nextt.next
        return first
