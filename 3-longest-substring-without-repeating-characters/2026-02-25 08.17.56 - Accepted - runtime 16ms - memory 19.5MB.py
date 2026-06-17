class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        m=0
        seen=set()
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[i])
            m=max(m,i-l+1)
        return m