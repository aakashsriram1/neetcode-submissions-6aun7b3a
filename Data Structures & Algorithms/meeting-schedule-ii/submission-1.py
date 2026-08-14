"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x : x.start)
        end_times = []
        heapq.heappush(end_times,intervals[0].end)
        for i in range(1,len(intervals)):
            curr_start, curr_end = intervals[i].start, intervals[i].end
            prev_end = end_times[0]
            if curr_start >= prev_end: 
                heapq.heappop(end_times)
            heapq.heappush(end_times,curr_end)

        return len(end_times)
