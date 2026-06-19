# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k==0:
            return head
        temp=head
        c=0
        while temp!=None:
            c+=1
            temp=temp.next
        if k>=c:
            k=k%c
        temp=head
        while temp.next!=None:
            temp=temp.next
        temp.next=head
        ptr=head
        for i in range(c-k-1):
            ptr=ptr.next
        new_head=ptr.next
        ptr.next=None
        return new_head
