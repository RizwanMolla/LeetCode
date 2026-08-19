class Solution:
    def subarrayBitwiseORs(self, arr):
        result = set()
        curr = set()
        
        for num in arr:
            new_curr = {num}
            for prev in curr:
                new_curr.add(prev | num)
            curr = new_curr
            result.update(curr)
        
        return len(result)
