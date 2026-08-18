class Solution:
    def largestOddNumber(self, num: str) -> str:
        ans=-1
        for i in range(len(num)-1, -1,-1):
            if int(num[i])%2:
                ans=i
                break
        if ans==-1:
            return ""
        else: 
            return num[:i+1]