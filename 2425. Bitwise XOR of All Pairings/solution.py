class Solution:
    def xorAllNums(self, nums1: list[int], nums2: list[int]) -> int:
        xor1, xor2 = 0, 0
        for num in nums1:
            xor1 ^= num
        for num in nums2:
            xor2 ^= num
        
        result = 0
        if len(nums2) % 2 == 1:
            result ^= xor1
        if len(nums1) % 2 == 1:
            result ^= xor2
        
        return result


"""
Overview: The solution leverages the properties of XOR to optimize computation. Instead of generating all pairings explicitly, the solution observes that each number in one array contributes to the XOR operation depending on the size of the other array being odd or even. The XOR values for nums1 and nums2 are computed separately and selectively used to determine the final result. This approach ensures O(n + m) time complexity and O(1) space complexity.
"""