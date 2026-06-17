# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        q=0
        temp=head
        while temp is not None:
            q+=1
            temp=temp.next
        q=q-n
        if q==0:
            return head.next
        c=0
        temp2=head
        preptr=temp2
        while temp2 is not None:
            if c==q:
                preptr.next=temp2.next
                break
            else:
                preptr=temp2
                temp2=temp2.next
                c+=1
        return head

