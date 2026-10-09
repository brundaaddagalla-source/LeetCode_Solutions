class Solution:
    def minInsertions(self, s: str) -> int:
        # stack=[]
        # r=0
        # cl=0
        # for i in s:
        #     if i == '(':
        #         if cl == 1:
        #             r += 1
        #             cl = 0
        #         stack.append(i)
        #     elif i==')':
        #         if cl==0:
        #             cl+=1
        #         else:
        #             if stack == []:
        #                 r += 1
        #                 r += 1
        #             else:
        #                 stack.pop()
        #             cl = 0

        # if cl == 1:
        #     r += 1
        # return r + len(stack) * 2
        openb=0
        close=0
        i=0
        r=0
        while i<len(s):
            if s[i]==')':
                if i+1<len(s) and s[i+1]==')':
                    if openb==0:
                        r+=1
                    else:
                        openb-=1
                    i+=2
                else:
                    r+=1
                    if openb>0:
                        openb-=1
                    else:
                        r+=1
                    i+=1
            elif s[i]=='(':
                openb+=1
                i+=1
        return r+ openb*2
                
