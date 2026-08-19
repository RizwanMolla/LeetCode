from typing import List

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        indexed_nums = sorted((num, i) for i, num in enumerate(nums))
        groups = []
        
        temp_group = [indexed_nums[0]]
        for i in range(1, n):
            if indexed_nums[i][0] - indexed_nums[i - 1][0] <= limit:
                temp_group.append(indexed_nums[i])
            else:
                groups.append(temp_group)
                temp_group = [indexed_nums[i]]
        groups.append(temp_group)
        
        result = [0] * n
        for group in groups:
            sorted_group = sorted(group, key=lambda x: x[1])
            for idx, (value, original_index) in enumerate(sorted_group):
                result[original_index] = group[idx][0]
        
        return result


"""
The approach sorts the array while keeping track of indices, then groups elements that can be swapped based on the given limit. Each group is rearranged in its original index order to achieve the lexicographically smallest result. The time complexity is O(nlogn) due to sorting.
"""