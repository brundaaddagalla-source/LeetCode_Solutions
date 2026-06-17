class Solution:
    def processStr(self, s: str) -> str:
        r=[]
        for i in s:
            if i.isalpha():
                if i.islower():
                    r.append(i)
            elif i=="*":
                if len(r)!=0:
                    r.pop()
            elif i=="#":
                r=r*2
            elif i=="%":
                r=r[::-1]
        return "".join(r)
