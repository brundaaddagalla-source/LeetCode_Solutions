class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d={}
        for i in text:
            d[i]=d.get(i,0)+1
        m=float("inf")
        for i in "balon":
            if i not in d:
                return 0
            if i in ['l', 'o']:
                m=min(m, d[i]//2)
            else:
                m=min(m,d[i])
        return m