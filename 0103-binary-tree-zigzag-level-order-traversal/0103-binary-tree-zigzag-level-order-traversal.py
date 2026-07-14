# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        l=deque()
        l.append(root)
        f=[]
        c=0
        while len(l)>0:
            size=len(l)
            c+=1
            r=[]
            for i in range(size):
                x=l.popleft()
                r.append(x.val)
                if x.left is not None:
                    l.append(x.left)
                if x.right is not None:
                    l.append(x.right)
            if c%2==1:
                f.append(r)
            else:
                f.append(r[::-1])
        return f