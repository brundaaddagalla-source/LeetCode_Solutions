# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def is_mirror(t1,t2):
            if t1==None and t2==None: return True
            elif t1==None or t2==None or t1.val!=t2.val: return False
            else: 
                return is_mirror(t1.left,t2.right) and is_mirror(t2.left,t1.right)

        return is_mirror(root.left, root.right)