class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False
        d1={}
        d2={}
        for i in range(len(word1)):
            d1[word1[i]]=d1.get(word1[i], 0)+1
            d2[word2[i]]=d2.get(word2[i], 0)+1
        k1=list(d1.keys())
        k2=list(d2.keys())
        f1=list(d1.values())
        f2=list(d2.values())
        if sorted(k1)!=sorted(k2): return False
        if sorted(f1)!=sorted(f2): return False
        return True