from heapq import heappush, heappop, heapify
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        free_rooms = list(range(n))
        heapify(free_rooms)

        busy_rooms = []
        count = [0] * n

        for start, end in meetings:
            while busy_rooms and busy_rooms[0][0] <= start:
                end_time, room = heappop(busy_rooms)
                heappush(free_rooms, room)

            duration = end - start

            if free_rooms:
                room = heappop(free_rooms)
                heappush(busy_rooms, (end, room))
                count[room] += 1
            else:
                end_time, room = heappop(busy_rooms)
                new_end = end_time + duration
                heappush(busy_rooms, (new_end, room))
                count[room] += 1

        max_meetings = max(count)
        for i in range(n):
            if count[i] == max_meetings:
                return i
