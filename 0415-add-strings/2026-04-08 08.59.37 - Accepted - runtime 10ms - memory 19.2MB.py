class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        c=0
        x=""
        i=len(num1)-1
        j=len(num2)-1
        while i>=0 or j>=0 or c:
            a=int(num1[i]) if i>=0 else 0
            b=int(num2[j]) if j>=0 else 0
            s=a+b+c
            x=str(s%10)+x
            c=s//10
            i-=1
            j-=1
        return x    