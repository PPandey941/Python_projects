
from datetime import datetime
class money:
    def __init__(self):
        pass
    def time_calulation(self, starting_time, ending_time):
        start_time = starting_time
        end_time = ending_time
        t1 = datetime.strptime(start_time, "%H:%M")
        t2 = datetime.strptime(end_time, "%H:%M")
        delta = t2 - t1
        time_in_hours = delta.total_seconds()/3600
        print(f"Time difference is {time_in_hours} hours")
        return time_in_hours

    def amount_to_pay(self, time):
        if time <= 1:
            print("Pay Rs. 80")
        elif time >1 and time <= 2:
            print("Pay Rs.180")
        elif time > 2 and time <= 3:
            print("Pay Rs.280")
        elif time > 3:
            money = 280 + (time - 3)* 150
            print(f"Pay Rs.{money}")
# m = money()
# m.amount_to_pay(5)
# m.time_calulation("12:56", "13:56")