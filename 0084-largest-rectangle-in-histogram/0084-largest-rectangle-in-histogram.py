class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        max_area=-1
        for i in range(len(heights)):
            start=i
            while stack and stack[-1][1]>heights[i]:
                p,h=stack.pop()
                max_area=max(max_area, h*(i-p))
                start=p
            stack.append([start, heights[i]])
        while stack:
            p,h=stack.pop()
            max_area=max(max_area, h*(len(heights)-p))
        return max_area

        #https://www.youtube.com/watch?v=zx5Sw9130L0
            