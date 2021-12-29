"""
* Problem: Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum
number of conference rooms required. Example: Input: [[0,30],[5,10],[15,20]] -> Output: 2
* Algorithm: Sort the conference intervals by the starting time.
The first conference intervals[0] should be in a room.
The second conference intervals[1], if intervals[1][0] <= intervals[0][1], then the second conference should be in a new
room; otherwise, it can be in the same room with intervals[0]
The third conference intervals[2], if intervals[2][0] <= min(intervals[0][1], intervals[1][1]) then the third conference
should be in a new room; otherwise, it can be in the same room with min(intervals[0][1], intervals[1][1]).
So one can use heap to store rooms.
* Time-complexity: O(nlogn)
- O(n*logn) due to sorting intervals
- Each step of pushing/poping intervals[i][1], it takes at most log(n) steps so totally it takes at most O(nlogn)
* Space-complexity: O(n)
"""

import heapq

def MeetingRoomII_heapq(intervals):
    n = len(intervals)
    if n == 0:
        return 0

    sorted_intervals = sorted(intervals, key=lambda x:x[0])
    rooms = [sorted_intervals[0][1]]
    heapq.heapify(rooms)
    for i in range(1, n):
        if rooms[0] <= sorted_intervals[i][0]:
            heapq.heappop(rooms)
            heapq.heappush(rooms, sorted_intervals[i][1])
        else:
            heapq.heappush(rooms, sorted_intervals[i][1])
    return len(rooms)

def MeetingRoomII_bruteforce(intervals):
    n = len(intervals)
    sorted_intervals = sorted(intervals, key=lambda x:x[0])

    print(sorted_intervals)

    rooms = [[]]
    rooms[0].append(sorted_intervals[0])
    for i in range(1, n):
        need_new_room = True
        for j in range(len(rooms)):
            if rooms[j][-1][1] <= sorted_intervals[i][0]:
                need_new_room = False
                rooms[j].append(sorted_intervals[i])
                break
        if need_new_room:
            rooms.append([sorted_intervals[i]])
    return len(rooms)


a = [[0,30],[5,10],[15,20]]
# a = [[7,10],[2,4]]
a = [[1293,2986],[848,3846],[4284,5907],[4466,4781],[518,2918],[300,5870]]
print(MeetingRoomII(a))
