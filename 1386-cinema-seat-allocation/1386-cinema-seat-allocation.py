class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # seats = [[0] * 10 for i in range(n)]
        s={}
        for i in reservedSeats:
            i[0]-=1
            i[1]-=1
            if i[0] not in s:
                s[i[0]]=[0]*10
                s[i[0]][i[1]]=1
            else:
                s[i[0]][i[1]]=1
        c=2*(n-len(s))
        for i in s:
            left=True
            for j in range(1,5):
                if s[i][j]==1:
                    left=False
                    break
            middle=True
            for j in range(3,7):
                if s[i][j]==1:
                    middle=False
                    break
            right=True
            for j in range(5,9):
                if s[i][j]==1:
                    right=False
                    break
            if left and right: c+=2
            elif left: c+=1
            elif right: c+=1
            elif middle: c+=1
        return c
