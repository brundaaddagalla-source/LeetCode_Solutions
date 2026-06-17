# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # r=[]
        # while head:
        #     r.append(head.val)
        #     head=head.next
        # r.reverse()
        # temp=ListNode(0)
        # ptr=temp
        # for i in r:
        #     temp.next=ListNode(i)
        #     temp=temp.next
        # temp.next=None
        # return ptr.next

        temp=head
        prev=None
        while temp:
            next=temp.next
            temp.next=prev
            prev=temp
            temp=next
        return prev