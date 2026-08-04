class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        s=[0]*10
        g=[0]*10
        c=0
        b=0
        for i in range(len(guess)):
            if secret[i]==guess[i]:
                b+=1
            else:
                s[int(secret[i])]+=1
                g[int(guess[i])]+=1
        for i in range(10):
            c+=min(s[i], g[i])
        return str(b)+"A"+str(c)+"B"