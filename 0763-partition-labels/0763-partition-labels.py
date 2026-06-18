class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d={}
        r=[]
        for i in set(s):
            d[i]=s.rfind(i)
        end=-1
        start=0
        for i in range(len(s)):
            end=max(end, d[s[i]])
            if i==end:
                r.append(end-start+1)
                start=i+1
        return r
