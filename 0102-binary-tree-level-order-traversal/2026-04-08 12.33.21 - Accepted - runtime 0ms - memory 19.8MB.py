# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        l=deque()
        l.append(root)
        f=[]
        while len(l)>0:
            size=len(l)
            r=[]
            for i in range(size):
                x=l.popleft()
                r.append(x.val)
                if x.left is not None:
                    l.append(x.left)
                if x.right is not None: 
                    l.append(x.right) 
            f.append(r)
        return f
