class Solution:
    def myAtoi(self, s: str) -> int:
        f=""
        s=s.lstrip()
        for i in s:
            if i in "+-1234567890":
                if (i=="-" or i=="+" or i==" ") and f:
                    break
                if f=="" and (i=="+" or i=="-"):
                    f+=i
                elif i.isdigit():
                    f+=i
                else:
                    break
            else:
                break
        if f=="" or f=="-" or f=="+":
            return 0
        else:
            f=int(f)
            # if f[0]=="-":
            #     sign=1
            # else:
            #     sign=0
            # f=abs(int(f))
            # if sign:
            #     f=-f
            if f<(-2**31):
                return -2**31
            elif f>(2**31)-1:
                return (2**31)-1
            else:
                return f