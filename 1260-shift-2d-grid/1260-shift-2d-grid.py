class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        k=k%(m*n)
        l=[]
        r=[]
        for i in range(m):
            for j in range(n):
                l.append(grid[i][j])
        for i in range(k):
            r.append(l.pop())
        r=r[::-1]
        r.extend(l)
        f=[]
        c=0
        for i in range(m):
            x=[]
            for j in range(n):
                x.append(r[c])
                c+=1
            f.append(x)
        return f
            
        