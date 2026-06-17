# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        temp=head
        curr=temp
        prev=None
        while temp:
            if temp.val==val:
                if prev:
                    prev.next=temp.next
                else:
                    head=temp.next
                temp=temp.next
            else:
                prev=temp
                temp=temp.next
        return head