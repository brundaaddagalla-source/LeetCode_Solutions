class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        du={}
        dl={}
        for i in range(len(word)):
            if word[i].isupper() and word[i] not in du:
                du[word[i]]=i
            elif word[i].islower():
                dl[word[i]]=i
        c=0
        i=0
        j=0
        for i in dl:
            if i.upper() in du:
                if dl[i]<du[i.upper()]:
                    c+=1
        return c
