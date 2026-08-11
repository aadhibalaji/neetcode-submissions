class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        

        intervals.append(newInterval)
        intervals.sort(key = lambda i : i[0])

        res = []
        res.append(intervals[0])

        lastEnd = intervals[0][1]

        for start, end in intervals[1:]:
            lastEnd = res[-1][1]
            
            if start <= lastEnd:
                res[-1][1] = max(lastEnd, end)
            else:
                res.append([start, end])

            

        return res
    
            

        

            

