class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals)==0:
            return 0
        intervals.sort(key=lambda x:x[1])
        c=1
        prev=0
        for i in range(1, len(intervals)):
            if intervals[i][0]>=intervals[prev][1]:
                prev=i
                c+=1
        return len(intervals)-c
        #https://www.youtube.com/watch?v=XsrJgwGlRoc&t=108s