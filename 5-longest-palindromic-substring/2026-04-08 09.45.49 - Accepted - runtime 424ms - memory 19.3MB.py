class Solution:
    def longestPalindrome(self, s: str) -> str:
        mini=""
        for i in range(len(s)): 
            # for j in range(i,len(s)): 
                # if s[i:j+1]==s[i:j+1][::-1] and len(s[i:j+1])>len(mini): 
                #     mini=(s[i:j+1]) 
            j=0
            while i-j>=0 and i+j<len(s) and s[i-j]==s[i+j]:
                if (2*j+1)>len(mini):
                    mini=s[i-j:i+j+1]
                j+=1
            j=0
            while i-j>=0 and i+j+1<len(s) and s[i-j]==s[i+j+1]:
                if (2*j+2)>len(mini):
                    mini=s[i-j:i+j+2]
                j+=1                
        return mini