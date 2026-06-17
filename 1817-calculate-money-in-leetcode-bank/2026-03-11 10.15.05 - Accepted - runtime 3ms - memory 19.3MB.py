class Solution:
    def totalMoney(self, n: int) -> int:
        d={1:1,2:2,3:3,4:4,5:5,6:6,7:7}
        s=0
        i=1
        while n>0:
            s+=d[i]
            d[i]+=1
            i+=1
            if i==8:
                i=1
            n-=1
        return s