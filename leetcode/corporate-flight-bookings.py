class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        seats = [0] * n
        for firsti, lasti, seatsi in bookings:
            seats[firsti - 1] += seatsi
            if lasti < n:
                seats[lasti] -= seatsi
    
        for i in range(1, n):
            seats[i] += seats[i - 1]
        return seats
        