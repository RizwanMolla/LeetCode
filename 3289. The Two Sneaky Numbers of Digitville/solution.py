from collections import Counter
from typing import List

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        return [num for num, freq in count.items() if freq == 2]
