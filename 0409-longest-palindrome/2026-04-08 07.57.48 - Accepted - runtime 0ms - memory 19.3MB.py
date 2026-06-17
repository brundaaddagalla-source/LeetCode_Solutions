class Solution:
    def longestPalindrome(self, s: str) -> int:
        # mini=0
        # for i in range(len(s)):
        #     for j in range(i,len(s)):
        #         if s[i:j+1]==s[i:j+1][::-1] and len(s[i:j+1])>mini:
        #             mini=len(s[i:j+1])
        # return mini
        d={}
        for i in set(s):
            d[i]=s.count(i)
        f=0
        r=0
        for i in d.values():
            if i%2==0:
                r+=i
            else:
                r+=i-1
                f=1
        if f==1:
            r+=1
        return r
