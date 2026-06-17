class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        map1={}
        map2={}
        for i,j in zip(s,t):
            if i in map1 and map1[i]!=j:
                return False
            if j in map2 and map2[j]!=i:
                return False
            map1[i]=j
            map2[j]=i
        return True