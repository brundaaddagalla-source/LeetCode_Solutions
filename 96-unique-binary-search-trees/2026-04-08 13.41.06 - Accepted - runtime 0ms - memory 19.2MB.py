class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 0
        # def build(start, end):
        #     if start > end:
        #         return [None]
        #     trees = []
        #     for i in range(start, end + 1):
        #         left_trees = build(start, i - 1)
        #         right_trees = build(i + 1, end)
        #         for l in left_trees:
        #             for r in right_trees:
        #                 root = TreeNode(i)
        #                 root.left = l
        #                 root.right = r
        #                 trees.append(root)
        #     return trees
        # return len(build(1, n))
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,n+1):
            for j in range(1,i+1):
                dp[i]+=dp[i-j]*dp[j-1]
        return dp[n]