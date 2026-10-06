class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        s1=s1.split()
        s2=s2.split()
        d1={}
        for i in s1:
            d1[i]=d1.get(i,0)+1
        for i in s2:
            d1[i]=d1.get(i,0)+1
        r1=[]
        for i in d1:
            if d1[i]==1:
                r1.append(i)
        return (r1) # ^ operator is symmetric difference operator, it returns uncommon elements from both the sets