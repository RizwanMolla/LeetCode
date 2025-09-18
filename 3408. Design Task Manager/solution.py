import heapq
from typing import List, Dict, Tuple

class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.task_map: Dict[int, Tuple[int, int]] = {}  # taskId -> (priority, userId)
        self.heap: List[Tuple[int, int, int]] = []      # (-priority, -taskId, userId)
        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_map[taskId] = (priority, userId)
        heapq.heappush(self.heap, (-priority, -taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        if taskId in self.task_map:
            userId = self.task_map[taskId][1]
            self.task_map[taskId] = (newPriority, userId)
            heapq.heappush(self.heap, (-newPriority, -taskId, userId))

    def rmv(self, taskId: int) -> None:
        if taskId in self.task_map:
            del self.task_map[taskId]  # lazy removal

    def execTop(self) -> int:
        while self.heap:
            neg_priority, neg_taskId, heap_userId = heapq.heappop(self.heap)
            taskId = -neg_taskId
            real_priority = -neg_priority

            if taskId in self.task_map:
                cur_priority, cur_userId = self.task_map[taskId]
                # Validate both priority and userId match the current mapping
                if cur_priority == real_priority and cur_userId == heap_userId:
                    del self.task_map[taskId]
                    return cur_userId
            # else stale entry; continue popping
        return -1
