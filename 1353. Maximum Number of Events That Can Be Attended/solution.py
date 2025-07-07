import heapq

class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:
        events.sort()
        min_heap = []
        day = 0
        event_id = 0
        total_attended = 0
        n = len(events)
        
        while event_id < n or min_heap:
            if not min_heap:
                day = events[event_id][0]
            
            while event_id < n and events[event_id][0] <= day:
                heapq.heappush(min_heap, events[event_id][1])
                event_id += 1
            
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)
            
            if min_heap:
                heapq.heappop(min_heap)
                total_attended += 1
            
            day += 1
        
        return total_attended
