class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        cnt = 0
        i = 0 
        intervals.sort(key = lambda x:x[1])
        print(intervals)
        prev = intervals[0][1]
        
        for interval in intervals[1:]:
            if prev > interval[0]:
                cnt+=1
            else:
                prev = interval[1]
        
        return cnt