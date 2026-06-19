# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getMid(self, head):
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
    def merge(self, left, right):
        ptr=ListNode(0)
        temp=ptr
        while left!=None and right!=None:
            if left.val<=right.val:
                temp.next=left
                temp=temp.next
                left=left.next
            else:
                temp.next=right
                temp=temp.next
                right=right.next
        while left!=None:
            temp.next=left
            temp=temp.next
            left=left.next
        while right!=None:
            temp.next=right
            temp=temp.next
            right=right.next
        return ptr.next
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        left=head
        right=self.getMid(head)
        temp=right.next
        right.next=None
        right=temp
        left=self.sortList(left)
        right=self.sortList(right)
        return self.merge(left, right)
        