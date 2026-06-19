# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k==0 or k==1:
            return head
        temp=head
        c=0
        while temp!=None:
            c+=1
            temp=temp.next
        temp=ListNode(0)
        temp.next=head
        ptr=head
        prev=temp
        for i in range(c//k):
            tail=ptr
            prev2=None
            for j in range(0,k):
                next=ptr.next
                ptr.next=prev2
                prev2=ptr
                ptr=next
            prev.next=prev2
            tail.next=ptr
            prev=tail
        return temp.next