# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next or left==right:
            return head
        temp=head
        lprev=None
        c=1
        while c<left:
            lprev=temp
            temp=temp.next
            c+=1
        left=temp
        prev=None
        while c<=right:
            next=temp.next
            temp.next=prev
            prev=temp
            temp=next
            c+=1
        left.next=temp
        if lprev:
            lprev.next=prev
            return head
        else:
            return prev