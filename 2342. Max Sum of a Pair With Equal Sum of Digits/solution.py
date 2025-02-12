from collections import defaultdict

class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        def sum_of_digits(num):
            return sum(int(digit) for digit in str(num))
        
        digit_sum_map = defaultdict(list)
        for num in nums:
            s = sum_of_digits(num)
            digit_sum_map[s].append(num)
        
        max_sum = -1
        for s in digit_sum_map:
            if len(digit_sum_map[s]) >= 2:
                sorted_nums = sorted(digit_sum_map[s], reverse=True)
                current_sum = sorted_nums[0] + sorted_nums[1]
                if current_sum > max_sum:
                    max_sum = current_sum
        
        return max_sum