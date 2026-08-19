class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        
        total_seats = corridor.count('S')
        # If total seats is odd or zero, no valid division
        if total_seats == 0 or total_seats % 2 != 0:
            return 0
        
        ways = 1
        seat_count = 0
        plant_count = 0
        
        for ch in corridor:
            if ch == 'S':
                seat_count += 1
                # When we complete a section of 2 seats
                if seat_count % 2 == 0:
                    ways = (ways * (plant_count + 1)) % MOD
                    plant_count = 0
            else:  # ch == 'P'
                # Only count plants after finishing a section
                if seat_count % 2 == 0 and seat_count > 0:
                    plant_count += 1
        
        return ways
