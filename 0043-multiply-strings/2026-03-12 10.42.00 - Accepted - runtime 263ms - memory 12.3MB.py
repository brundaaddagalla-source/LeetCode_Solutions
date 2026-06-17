class Solution(object):
    def multiply(self, num1, num2):
        # num1=int(num1)
        # num2=int(num2)
        # return str(num1*num2)

        if num1=="0" or num2=="0":
            return "0"
        x=len(num1)
        y=len(num2)
        r=0
        for i in range(x-1,-1,-1):
            ps=0
            for j in range(y-1,-1,-1):
                a=int(num1[i])
                b=int(num2[j])
                ps+= a*b* 10**(y-j-1)
            r+= ps * 10**(x-i-1)
        return str(r)