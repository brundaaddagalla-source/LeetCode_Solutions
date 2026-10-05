class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        r=[0]
        sc=0
        for i in s:
            if i=="(":
                r.append(0)
            else:
                c=r.pop()
                if c==0: c+=1
                else: c=(2*c)
                r[-1]+=c
        return r[-1]