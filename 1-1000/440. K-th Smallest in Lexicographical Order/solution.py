class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        """
        Find the k-th lexicographically smallest integer in range [1, n].
        
        Approach: Navigate a conceptual trie structure efficiently
        - Numbers in lexicographical order form a 10-ary trie
        - Calculate count of numbers in each subtree
        - Skip entire subtrees when k-th number isn't there
        - Move to next sibling or go deeper accordingly
        
        Time: O(log^2 n), Space: O(1)
        """
        curr = 1  # Start from the first number
        k -= 1    # Convert to 0-indexed (we want k-1 more numbers)
        
        while k > 0:
            # Count numbers between curr and curr+1 prefixes
            count = self._count_numbers_with_prefix(curr, curr + 1, n)
            
            if count <= k:
                # k-th number is not in current subtree
                # Skip this entire subtree and move to next sibling
                k -= count
                curr += 1
            else:
                # k-th number is in current subtree
                # Go one level deeper (multiply by 10)
                k -= 1  # Count current number
                curr *= 10
        
        return curr
    
    def _count_numbers_with_prefix(self, prefix1: int, prefix2: int, n: int) -> int:
        """
        Count numbers in range [1, n] that have prefix1 but not prefix2.
        This counts all numbers in the subtree rooted at prefix1.
        
        Examples:
        - prefix1=1, prefix2=2, n=13: counts [1, 10, 11, 12, 13] = 5
        - prefix1=10, prefix2=11, n=13: counts [10] = 1
        """
        count = 0
        
        while prefix1 <= n:
            # Count numbers in current level
            # min(n + 1, prefix2) - prefix1 gives count in this level
            count += min(n + 1, prefix2) - prefix1
            
            # Move to next level
            prefix1 *= 10
            prefix2 *= 10
        
        return count