class Solution:
    def convert(self, s: str, numRows: int) -> str:
        f=[""]*numRows
        if numRows==1 or len(s)<=numRows:
            return s
        i=0
        step=0
        for j in s:
            f[i]+=j
            if i==0:
                step=1
            elif i==numRows-1:
                step=-1
            i+=step
        return "".join(f)
