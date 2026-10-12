class BusBooking:

    def __init__(self, n: int):
        self.booked = set()
        self.costs = {}
        self.total_time = 0

    def toggle(self, seat: str) -> None:
        if seat in self.booked:
            self.booked.remove(seat)
            self.total_time -= self.costs.pop(seat)
        else:
            letter = seat[0]
            row = seat[1:]
            adjacent = None

            if letter == 'A':
                adjacent = 'B' + row
            elif letter == 'D':
                adjacent = 'C' + row

            cost = 3 if adjacent in self.booked else 1

            self.booked.add(seat)
            self.costs[seat] = cost
            self.total_time += cost

    def getTotalTime(self) -> int:
        return self.total_time

    def getMinTime(self) -> int:
        return len(self.booked)

# Your BusBooking object will be instantiated and called as such:
# obj = BusBooking(n)
# obj.toggle(seat)
# param_2 = obj.getTotalTime()
# param_3 = obj.getMinTime()