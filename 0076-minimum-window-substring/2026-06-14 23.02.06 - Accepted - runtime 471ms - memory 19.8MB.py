class Solution:
    def minWindow(self, s: str, t: str) -> str:

        def contains(d1,d2):
            for i in d1:
                if d1[i]>d2.get(i,0):
                    return False
            return True
        
        if len(t)>len(s):
            return ""
        #character map for substring
        d1={}
        for i in t:
            d1[i]=d1.get(i,0)+1
        #character map for main string using pointers
        d2={}
        for i in set(s):
            d2[i]=0
        left=0
        minLen=float('inf')
        mins=0
        for right in range(len(s)):
            d2[s[right]]+=1
            while contains(d1,d2):
                if right-left+1<minLen:
                    minLen=right-left+1
                    mins=left
                d2[s[left]]-=1
                left+=1
        return "" if minLen==float('inf') else s[mins:mins+minLen]

#https://www.youtube.com/watch?v=SdeaOYoPhIs