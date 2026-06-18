class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # d={"(":0, ")":0}
        # for i in s:
        #     d[i]=d.get(i,0)+1
        # return abs(d["("]-d[")"])
        stack=[]
        c=0
        for i in s:
            if i=="(":
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                else:
                    c+=1
        return len(stack)+c