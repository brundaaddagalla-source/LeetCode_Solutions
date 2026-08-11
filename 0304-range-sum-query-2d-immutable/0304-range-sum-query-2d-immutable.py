class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix
        self.prefix=[i[:] for i in matrix]
        for i in range(len(matrix)):
            for j in range(1,len(matrix[0])):
                self.prefix[i][j]+=self.prefix[i][j-1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum1=0
        for i in range(row1, row2+1):
            if col1==0:
                sum1+=self.prefix[i][col2]
            else:
                sum1+=(self.prefix[i][col2]-self.prefix[i][col1-1])
        return sum1



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)https://assets.leetcode.com/uploads/2021/03/14/sum-grid.jpg$0