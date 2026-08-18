class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        p=[]
        ns=""
        for i in s:
            ns+=i
            if i==")":
                p.pop()
                if p==[]:
                    stack.append(ns)
                    ns=""
            else:
                p.append(i)
        print(stack)
        r=""
        for i in stack:
            for j in range(1, len(i)-1):
                r+=i[j]
        return r
