n = 2
brightness = 1
intervals = [[0, 0], [2, 2]]
intervals.sort()

active_time = 0

start, end = intervals[0]

for s, e in intervals[1:]:
    if s <= end + 1:
        end = max(end, e)
    else:
        active_time += end - start + 1
        start, end = s, e

active_time += end - start + 1

bulbs_needed = (brightness + 2) // 3

return bulbs_needed * active_time
