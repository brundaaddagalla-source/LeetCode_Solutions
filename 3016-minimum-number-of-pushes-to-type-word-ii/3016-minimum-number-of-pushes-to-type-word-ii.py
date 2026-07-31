class Solution:
    def minimumPushes(self, word: str) -> int:
        d={}
        for i in word:
            d[i]=d.get(i,0)+1
        x=sorted(d.values(), reverse=True)
        c=0
        if len(d)<=8:
            c=sum(list(d.values()))
        elif len(d)<=16:
            c+=sum(x[:8])
            c+=sum(2*i for i in x[8:])
        elif len(d)<=24:
            c+=sum(x[:8])
            c+=sum(2*i for i in x[8:16])
            c+=sum(3*i for i in x[16:])
        else:
            c+=sum(x[:8])
            c+=sum(2*i for i in x[8:16])
            c+=sum(3*i for i in x[16:24])
            c+=sum(4*i for i in x[24:])

        return c
            

