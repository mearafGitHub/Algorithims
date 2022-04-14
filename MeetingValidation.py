class Interval:
    def __int__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def meeting(self, intervals):
        intervals.sort(key=lambda x: x.start)
        for i in range(1, len(intervals)):
            prev = intervals[0]
            nxt = intervals[1]
            if prev.end > nxt.start:
                return False

        return True

meetings = []
for i in range(11):
    a = Interval()
    a.start = i
    a.end = i+5
    meetings.append(a)

solve = Solution()
print(solve.meeting(meetings))
