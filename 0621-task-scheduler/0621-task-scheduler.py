class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d={}
        for i in tasks:
            d[i]=d.get(i,0)+1
        f=max(d.values())
        c=sum(i==f for i in d.values())
        return max(len(tasks), (f-1)*(n+1)+c)