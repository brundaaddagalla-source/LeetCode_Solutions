# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr=head
        if ptr==None or ptr.next==None  :
            return head
        head=ptr.next
        preptr=None
        while ptr and ptr.next:
            f=ptr
            s=ptr.next
            f.next=s.next
            s.next=f
            if preptr:
                preptr.next=s
            preptr=f
            ptr=f.next
        return head