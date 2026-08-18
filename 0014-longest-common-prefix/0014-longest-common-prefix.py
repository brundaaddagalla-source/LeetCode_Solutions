class Solution(object):
    def longestCommonPrefix(self, strs):
        # strs.sort()
        # first=strs[0]
        # last=strs[-1]
        # lmin=min(len(first),len(last))
        # i=0
        # while i<lmin and first[i]==last[i]:
        #     i+=1
        # return(first[0:i])
        n=201
        for i in strs:
            if len(i)<n:
                n=len(i)
        for i in range(n):
            for j in range(len(strs)):
                if strs[0][i]!=strs[j][i]:
                    return strs[0][:i]
        return strs[0][:n]