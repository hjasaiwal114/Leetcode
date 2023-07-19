"""
435 Non -overlaping intervals
Given an array of intervals where intervals[i] = [start, end] , retrn the minimum number of intervals
you need to remove to make the rest of the intervals non-overlapping.
"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        n = len(intervals)

        prev = 0
        count = 1

        for i in range(1, n):
            if interals[i][0] >= intervals[prev][1]:
                prev = i
                count += 1
        return n - count
