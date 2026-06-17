# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        l=[]
        while head is not None:
            l.append(head.val)
            head=head.next
        maxi=-1
        for i in range(len(l)):
            if l[i]+l[len(l)-i-1] > maxi:
                maxi=l[i]+l[len(l)-i-1]
        return maxi
