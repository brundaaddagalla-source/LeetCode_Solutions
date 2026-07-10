class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        o=[0]*len(temperatures)
        stack=[]
        for i in range(len(temperatures)):
            while stack and temperatures[i]>stack[-1][1]:
                p,t=stack.pop()
                o[p]=i-p
            stack.append([i,temperatures[i]])
        return o

        #https://www.youtube.com/watch?v=cTBiBSnjO3c