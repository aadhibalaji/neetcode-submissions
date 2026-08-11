class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        

        if not intervals:
            return 0

        intervals.sort(key = lambda i : i[1])

        res = 0
        lastEnd = intervals[0][1]

        for start, end in intervals[1:]:

            if start < lastEnd:
                res += 1
            else: 
                lastEnd = end

        return res