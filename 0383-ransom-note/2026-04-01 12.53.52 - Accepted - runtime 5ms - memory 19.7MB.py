class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d1={}
        d2={}
        for i in set(ransomNote):
            d1[i]=ransomNote.count(i)
        for i in set(magazine):
            d2[i]=magazine.count(i)
        for i in d1:
            if (i not in d2) or (d1[i]>d2[i]):
                return False
        return True