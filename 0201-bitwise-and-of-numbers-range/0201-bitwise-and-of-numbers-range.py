class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # ans=left
        # for i in range(left, right+1):
        #     ans=ans&i
        # return ans
        c=0
        while left!=right:
            left=left >>1
            right=right >>1
            c+=1
        return left<<c

        #https://chatgpt.com/share/6a5f12d0-3a8c-83ee-954c-18c1a12f0481