from typing import List
from collections import deque
import bisect

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()  # Sort tasks by difficulty (ascending)
        workers.sort()  # Sort workers by strength (ascending)
        
        n, m = len(tasks), len(workers)
        
        # Helper function to check if k tasks can be assigned
        def can_assign(k):
            if k > m:  # Can't assign more tasks than workers
                return False
                
            # Take the k easiest tasks
            selected_tasks = tasks[:k]
            # Take k strongest workers
            selected_workers = workers[m-k:]
            
            # We'll use a multiset to track available workers
            # We need to remove specific workers efficiently
            # Using a sorted list and binary search for this purpose
            available = selected_workers.copy()
            pills_remaining = pills
            
            # Process tasks from hardest to easiest
            for i in range(k-1, -1, -1):
                task = selected_tasks[i]
                
                if not available:
                    return False
                
                # If the strongest worker can do the task without a pill
                if available[-1] >= task:
                    available.pop()  # Use the strongest worker
                # Try to use a pill
                elif pills_remaining > 0:
                    # If even the strongest worker with a pill can't do the task
                    if available[-1] + strength < task:
                        return False
                    
                    # Find the weakest worker who can do the task with a pill
                    idx = bisect.bisect_left(available, task - strength)
                    
                    if idx < len(available):
                        # Remove this worker
                        available.pop(idx)
                        pills_remaining -= 1
                    else:
                        return False
                else:
                    return False  # No more pills and strongest worker can't do the task
            
            return True
        
        # Binary search to find maximum k
        left, right = 0, min(n, m)
        result = 0
        
        while left <= right:
            mid = (left + right) // 2
            if can_assign(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return result