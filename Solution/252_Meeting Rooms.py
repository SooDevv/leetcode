from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) < 2: return True
        intervals.sort()
=        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True


if __name__ == '__main__':
    intervals = [[0,30],[60,240],[90,120]]
    result = Solution().canAttendMeetings(intervals)
    assert result == False