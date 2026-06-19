"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d={None: None}
        temp=head
        while temp!=None:
            new=Node(temp.val)
            d[temp]=new
            temp=temp.next
        temp=head
        while temp!=None:
            new=d[temp]
            new.next=d[temp.next]
            new.random=d[temp.random]
            temp=temp.next
        return d[head]
