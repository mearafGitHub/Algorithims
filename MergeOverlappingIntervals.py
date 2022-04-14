def overlapMerge(intervals):
    intervals.sort()
    merged_intervals = intervals[0]
    result = [merged_intervals]

    for interval in intervals:
        if merged_intervals[1] >= interval[0]:
            merged_intervals[1] = interval[1]
        else:
            merged_intervals = interval
            result.append(merged_intervals)
    return result


print(overlapMerge([[1, 3], [2, 6], [7, 8], [9, 10], [9, 13], [11, 15]]))
