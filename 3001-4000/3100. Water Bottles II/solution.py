class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drunk = numBottles
        empty = numBottles
        
        while empty >= numExchange:
            # Exchange bottles
            empty -= numExchange
            numExchange += 1
            drunk += 1
            empty += 1  # because we drink the new bottle immediately
        
        return drunk
