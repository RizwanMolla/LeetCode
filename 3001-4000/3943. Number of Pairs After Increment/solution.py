import numpy as np
from collections import defaultdict

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        m = len(nums2)
        nums2 = np.array(nums2, dtype=np.int64)
        diff = np.zeros(m + 1, dtype=np.int64)
        ans = []
        dirty = False

        for q in queries:
            if q[0] == 1:
                diff[q[1]] += q[3]
                diff[q[2] + 1] -= q[3]
                dirty = True
            else:
                if dirty:
                    delta = np.cumsum(diff[:m])
                    nums2 += delta
                    diff[:] = 0
                    dirty = False
                tot = q[1]
                
                count = 0
                for v in nums1:
                    count += np.sum(nums2 == tot - v)
                ans.append(int(count))

        return ans