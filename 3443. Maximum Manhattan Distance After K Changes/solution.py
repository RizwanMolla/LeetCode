class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        def max_subsequence_with_changes(dir1: str, dir2: str) -> int:
            max_len = curr_len = changes_used = 0
            for move in s:
                if move == dir1 or move == dir2:
                    curr_len += 1
                elif changes_used < k:
                    changes_used += 1
                    curr_len += 1
                else:
                    curr_len -= 1
                max_len = max(max_len, curr_len)
            return max_len

        opt1 = max_subsequence_with_changes("S", "E")
        opt2 = max_subsequence_with_changes("S", "W")
        opt3 = max_subsequence_with_changes("N", "E")
        opt4 = max_subsequence_with_changes("N", "W")

        return max(opt1, opt2, opt3, opt4)
