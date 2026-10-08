class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        d={}
        for i in deck:
            d[i]=d.get(i,0)+1
        values=list(d.values())
        if 1 in values:
            return False
        size=2
        while size<=min(values):
            if all(i%size==0 for i in values):
                return True
            size+=1
        return False