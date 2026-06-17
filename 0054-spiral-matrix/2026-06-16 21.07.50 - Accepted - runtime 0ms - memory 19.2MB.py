class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r=[]
        m,n=len(matrix), len(matrix[0])
        layers=(min(m,n)+1)//2
        for i in range(layers):
            for j in range(i,n-i):
                r.append(matrix[i][j])
            for j in range(i+1,m-i):
                r.append(matrix[j][n-i-1])
            if m-i-1!=i:
                for j in range(n-i-2, i-1,-1):
                    r.append(matrix[m-i-1][j])
            if n-i-1!=i:
                for j in range(m-i-2, i,-1):
                    r.append(matrix[j][i])
        return r