from typing import List

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left, right = 1, min(ranks) * (cars ** 2)  

        def canRepairInTime(T):
            total_cars = 0
            for r in ranks:
                total_cars += int((T // r) ** 0.5)  
                if total_cars >= cars:  
                    return True
            return False

        
        while left < right:
            mid = (left + right) // 2
            if canRepairInTime(mid):
                right = mid  
            else:
                left = mid + 1

        return left  
