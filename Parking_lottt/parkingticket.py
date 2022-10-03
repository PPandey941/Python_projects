
import random as r




class ticket:
    def __init__(self):
        self.total_parking_slots = 11
        self.bike_parking_slots = 2
        self.compact_car_slots = 3
        self.large_car_slots = 1
        self.electric_car_slots = 5
        self.tic_no = [tick for tick in range(1, self.total_parking_slots+1)]

    def assign_ticket(self):
        number = r.choice(self.tic_no)
        self.tic_no.remove(number)
        return number

