class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[0])
        print(points)
        c=1
        i=1
        end=points[0][1]
        while i<len(points):
            if points[i][0]<=end:
                end=min(end, points[i][1])
            else:
                c+=1
                end=points[i][1]
            i+=1
        return c
