class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = []
        prev_sorted = ""
        
        for w in words:
            sorted_w = ''.join(sorted(w))
            if sorted_w != prev_sorted:
                res.append(w)
                prev_sorted = sorted_w
        
        return res
