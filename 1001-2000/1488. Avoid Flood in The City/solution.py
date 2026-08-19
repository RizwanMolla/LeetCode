from bisect import bisect_right, insort
from typing import List

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        res = [-1] * n
        full = {}
        dry_days = []
        
        for i, lake in enumerate(rains):
            if lake > 0:
                if lake in full:
                    last_full_day = full[lake]
                    idx = bisect_right(dry_days, last_full_day)
                    
                    if idx == len(dry_days):
                        return []
                    
                    dry_day = dry_days.pop(idx)
                    res[dry_day] = lake
                    
                full[lake] = i
                res[i] = -1
            else:
                insort(dry_days, i)
                res[i] = 1
        
        return res