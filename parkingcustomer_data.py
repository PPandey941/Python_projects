
from parkingticket import ticket
t = ticket()
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M")
import csv
class customer:
    def __init__(self):
        self.header = ['ticket_no', 'name', 'vehicle_type', 'license_plate_number', 'phone_number', 'time']
        self.data = self.information()

    def information(self):
        name = input("enter your name")
        vehi = int(input("vehicle type"))
        if vehi == 1:
            vehicle_type = "bike"
            if t.bike_parking_slots == 0:
                print("No slots left")
            else:
                t.bike_parking_slots -= 1

        elif vehi == 2:
            vehicle_type = "compact car"
            if t.compact_car_slots == 0:
                print("No slots left")

            else:
                t.compact_car_slots -= 1
        elif vehi == 3:
            vehicle_type = "Large car"
            if t.large_car_slots == 0:
                print("No slots left")

            else:
                t.large_car_slots -= 1
        elif vehi == 4:
            vehicle_type = "electrical car or handicap vehicle"
            if t.electric_car_slots == 0:
                print("No slots left")

            else:
                t.electric_car_slots -= 1
        license_plate_no = input("license_plate_no")
        phone_no = input("phone number")
        time = current_time
        tickets = t.get_ticket_number()
        temp_tick = t.assign_ticket(tickets)
        t.clear_table()
        t.list_to_text(temp_tick)
        customer_data_list = [tickets, name, vehicle_type, license_plate_no, phone_no, time]
        print(f"Your ticket number is {tickets}")
        return customer_data_list

    def add_content(self, data_list):
        with open('parkingcustomers.csv', 'a') as p:
            writer = csv.writer(p)
            writer.writerow(data_list)




