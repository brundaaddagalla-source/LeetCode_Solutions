# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr=head
        r=[]
        while curr!=None:
            r.append(curr.val)
            curr=curr.next
        if r==r[::-1]:
            return True
        else:
            return False