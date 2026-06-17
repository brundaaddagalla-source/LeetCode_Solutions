# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        curr=head
        r=[]
        while curr!=None:
            r.append(curr.val)
            curr=curr.next
        if r==r[::-1]:
            return True
        else:
            return False