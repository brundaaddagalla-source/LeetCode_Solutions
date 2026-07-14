# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetsum: int) -> List[List[int]]:
        if root==None:
            return []
        stack=[]
        f=[]
        
        def dfs(root, targetsum):
            if root is None:
                return 
            stack.append(root.val)
            if root.left is None and root.right is None and root.val==targetsum:
                f.append(stack[:])
            else:
                dfs(root.left, targetsum-root.val)
                dfs(root.right, targetsum-root.val)
            stack.pop()
        dfs(root, targetsum)
        return f
