from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
from typing import List

class Router:

    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.queue = deque()  # store packets in FIFO
        self.seen = set()  # to detect duplicates
        self.dest_map = defaultdict(list)  # destination -> sorted list of timestamps

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)

        # check duplicate
        if packet in self.seen:
            return False

        # if memory full, remove oldest packet
        if len(self.queue) == self.memoryLimit:
            old_src, old_dst, old_time = self.queue.popleft()
            self.seen.remove((old_src, old_dst, old_time))
            # remove from dest_map
            lst = self.dest_map[old_dst]
            idx = bisect_left(lst, old_time)
            if idx < len(lst) and lst[idx] == old_time:
                lst.pop(idx)

        # add new packet
        self.queue.append(packet)
        self.seen.add(packet)
        self.dest_map[destination].append(timestamp)  # timestamps are increasing
        return True

    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return []
        source, destination, timestamp = self.queue.popleft()
        self.seen.remove((source, destination, timestamp))
        # remove from dest_map
        lst = self.dest_map[destination]
        idx = bisect_left(lst, timestamp)
        if idx < len(lst) and lst[idx] == timestamp:
            lst.pop(idx)
        return [source, destination, timestamp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        lst = self.dest_map.get(destination, [])
        left = bisect_left(lst, startTime)
        right = bisect_right(lst, endTime)
        return right - left
