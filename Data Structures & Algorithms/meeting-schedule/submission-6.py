"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
# 0,3 
# 3,6 
# 5,10

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals: 
            return True
        intervals.sort(key = lambda x: x.start)
        prev = intervals[0]
        for i in range(1,len(intervals)):
            curr_start,curr_end = intervals[i].start,intervals[i].end
            prev_start,prev_end = prev.start,prev.end

            if curr_start < prev_end:
                return False
            prev = intervals[i]
        return True