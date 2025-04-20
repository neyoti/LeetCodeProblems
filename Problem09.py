'''
56. Merge Intervals
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''

def mergeIntervals(intervals):
    intervals.sort()
    finalL = list()
    prev = intervals[0]
    
    for i in intervals[1:]:
        if i[0] <= prev[1]:
            prev[1] = max(i[1], prev[1])
        else:
            finalL.append(prev)
            prev = i
    finalL.append(prev)
    return finalL

intervals = [[1,3],[2,6],[8,10],[15,18]]

l = mergeIntervals(intervals)
print(l)
