from collections import Counter, deque
from string import ascii_lowercase

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        def is_k_repeated_subsequence(candidate: str, k: int) -> bool:
            idx = 0
            for char in s:
                if char == candidate[idx]:
                    idx += 1
                    if idx == len(candidate):
                        k -= 1
                        if k == 0:
                            return True
                        idx = 0
            return False

        # Step 1: Count character frequencies
        char_count = Counter(s)
        
        # Step 2: Filter characters that appear at least k times
        valid_chars = [ch for ch in ascii_lowercase if char_count[ch] >= k]
        
        # Step 3: BFS to build candidates
        queue = deque([""])
        longest_seq = ""
        
        while queue:
            current_seq = queue.popleft()
            for ch in valid_chars:
                next_seq = current_seq + ch
                if is_k_repeated_subsequence(next_seq, k):

                    if len(next_seq) > len(longest_seq) or (len(next_seq) == len(longest_seq) and next_seq > longest_seq):
                        longest_seq = next_seq
                    queue.append(next_seq)
        
        return longest_seq
