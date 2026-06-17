class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        low=0
        high=len(intervals)-1
        while low<=high:
            mid=low+(high-low)//2
            if intervals[mid][1]>=newInterval[0]:
                high=mid-1
            else:
                low=mid+1
        intervals.insert(low, newInterval)
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