class Solution:
    def reorganizeString(self, s: str) -> str:
        d={}
        for i in s:
            d[i]=d.get(i,0)+1
        if max(list(d.values()))>(len(s)+1)//2:
            return ""
        r=[0]*len(s)
        l=max(d,key=d.get)
        idx=0
        while d[l]>0:
            r[idx]=l
            idx+=2
            d[l]-=1
        for i in d:
            while d[i]>0:
                if idx>=len(s):
                    idx=1
                r[idx]=i
                idx+=2
                d[i]-=1
        return "".join(r)
