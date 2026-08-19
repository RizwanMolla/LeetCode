class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: list[list[int]]) -> int:
        conflicts_at_right = [[] for _ in range(n + 1)]

        for u, v in conflictingPairs:
            if u > v:
                u, v = v, u
            conflicts_at_right[v].append(u)

        total_valid_subarrays = 0
        
        max_left = 0
        second_max_left = 0

        gains = [0] * (n + 1)

        for current_right in range(1, n + 1):
            for left_val in conflicts_at_right[current_right]:
                if left_val > max_left:
                    second_max_left = max_left
                    max_left = left_val
                elif left_val > second_max_left:
                    second_max_left = left_val
            
            total_valid_subarrays += (current_right - max_left)

            if max_left > 0:
                gains[max_left] += (max_left - second_max_left)
        
        max_possible_gain = 0
        for gain_val in gains:
            max_possible_gain = max(max_possible_gain, gain_val)
            
        return total_valid_subarrays + max_possible_gain