# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1=""
        s2=""
        while l1!=None:
            s1+=str(l1.val)
            l1=l1.next
        while l2!=None:
            s2+=str(l2.val)
            l2=l2.next
        s1=s1[::-1]
        s2=s2[::-1]
        s=int(s1)+int(s2)
        r=ListNode(0)
        temp=r
        for i in str(s)[::-1]:
            temp.next=ListNode(int(i))
            temp=temp.next
        return r.next