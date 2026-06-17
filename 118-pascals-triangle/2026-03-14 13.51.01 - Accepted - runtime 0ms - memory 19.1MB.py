class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        r=[[1]]
        for i in range(1,numRows):
            j=0
            row=[]
            while j<=i:
                if j==0 or j==i:
                    row.append(1)
                else:
                    row.append(r[i-1][j-1]+r[i-1][j])
                j+=1
            r.append(row)
        return r