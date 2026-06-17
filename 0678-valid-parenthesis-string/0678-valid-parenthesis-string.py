class Solution:
    def checkValidString(self, s: str) -> bool:
        stack=[]
        star=[]
        for idx, i in enumerate(s):
            if i=="(":
                stack.append(idx)
            elif i=="*":
                star.append(idx)
            else:
                if stack: stack.pop()
                elif star: star.pop()
                else: return False
        while stack and star:
            if stack[-1]<star[-1]:
                stack.pop()
                star.pop()
            else:
                return False
        return len(stack)==0