class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        c=0
        for i in set(word.lower()):
            if (i.upper() in word) and (i in word):
                c+=1
        return c