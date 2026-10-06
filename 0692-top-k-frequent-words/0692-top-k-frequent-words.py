class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        d={}
        for i in words:
            d[i]=d.get(i,0)+1
        d=dict(sorted(d.items(), key= lambda x: (-x[1], x[0])))
        keys=list(d.keys())
        return keys[:k]