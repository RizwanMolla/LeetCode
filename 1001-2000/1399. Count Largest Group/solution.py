from collections import defaultdict

class Solution:
    def countLargestGroup(self, n: int) -> int:
        count = defaultdict(int)
        
        for i in range(1, n + 1):
            digit_sum = sum(int(d) for d in str(i))
            count[digit_sum] += 1

        max_size = max(count.values())
        return sum(1 for v in count.values() if v == max_size)
