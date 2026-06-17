class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        r=[]
        i=0
        while i<=len(intervals)-1:
            j=i
            while j+1<len(intervals) and  intervals[j+1][0]<=intervals[i][1]:
                intervals[i][1]=max(intervals[i][1], intervals[j+1][1])
                j+=1
            r.append(intervals[i])
            i=j+1
        return r