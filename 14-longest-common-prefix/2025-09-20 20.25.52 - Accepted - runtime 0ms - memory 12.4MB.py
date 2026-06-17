class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        first=strs[0]
        last=strs[-1]
        lmin=min(len(first),len(last))
        i=0
        while i<lmin and first[i]==last[i]:
            i+=1
        return(first[0:i])