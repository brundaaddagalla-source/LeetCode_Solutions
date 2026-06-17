class Solution:
    def compressedString(self, word: str) -> str:
        l=[]
        c=1
        for i in range(len(word)-1):
            if word[i]==word[i+1]:
                c+=1
            else:
                if c>9:
                    while c>9:
                        l.append(str(9))
                        l.append(word[i])
                        c=c-9
                    l.append(str(c))
                    l.append(word[i])
                else:
                    l.append(str(c))
                    l.append(word[i])
                c=1
        while c>9:
            l.append(str(9))
            l.append(word[i])
            c=c-9
        l.append(str(c))
        l.append(word[-1])
        return "".join(l)

        