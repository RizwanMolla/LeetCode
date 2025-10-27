class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0
        total = 0
        
        for row in bank:
            count = row.count('1')
            if count:  # non-empty row
                total += prev * count
                prev = count  # update previous row's device count
                
        return total
