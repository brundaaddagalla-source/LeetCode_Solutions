class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        cn=0
        cs=""
        for i in s:
            if i=="[":
                stack.append(cs)
                stack.append(cn)
                cs=""
                cn=0
            elif i=="]":
                n=stack.pop()
                st=stack.pop()
                cs=st+n*cs
            elif i.isdigit():
                cn=cn*10+int(i)
            elif i.isalpha():
                cs+=i
        return cs