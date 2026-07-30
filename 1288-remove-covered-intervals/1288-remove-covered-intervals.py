class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals=sorted(intervals, key=lambda x:(x[0], -x[1])) #sorting ascending based on starting time and for same start times, sort them in descending
        #eg, [[1,3], [1,4]], if not sorted in descending by the end, then 4<=3 would be false, and the interval would not be removed
        i=1
        while i<len(intervals):
            # intervals[i][0]<=intervals[i-1][0]: we are not keeping this condition because the intervals array is alread sorted so this would be true always
            if intervals[i][1]<=intervals[i-1][1]:
                intervals.pop(i)
            else:
                i+=1
        return len(intervals)