from typing import List
from collections import deque

class Solution:
    def maxCandies(self, status: List[int], candies: List[int],
                   keys: List[List[int]], containedBoxes: List[List[int]],
                   initialBoxes: List[int]) -> int:
        
        n = len(status)
        queue = deque()
        seen = set()
        have_keys = set()
        waiting = set()
        total_candies = 0

        for box in initialBoxes:
            if status[box] == 1:
                queue.append(box)
            else:
                waiting.add(box)

        while queue:
            curr = queue.popleft()
            if curr in seen:
                continue
            seen.add(curr)
            total_candies += candies[curr]

            # Add new keys and open any waiting box
            for key in keys[curr]:
                have_keys.add(key)
                if key in waiting:
                    queue.append(key)
                    waiting.remove(key)

            # Add contained boxes to process
            for new_box in containedBoxes[curr]:
                if status[new_box] == 1 or new_box in have_keys:
                    queue.append(new_box)
                else:
                    waiting.add(new_box)

        return total_candies
