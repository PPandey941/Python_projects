import random as r
tick_list = []
class ticket:
    def __init__(self):
        self.total_parking_slots = 11
        self.bike_parking_slots = 2
        self.compact_car_slots = 3
        self.large_car_slots = 1
        self.electric_car_slots = 5

    def create_a_list(self):
        tic_no = [tick for tick in range(1, self.total_parking_slots+1)]
        return tic_no

    def list_to_text(self, enter_a_list):
        with open('ticket.txt', 'w') as fp:
            for item in enter_a_list:
                fp.write("%s\n" % item)

    def clear_table(self):
        f= open("ticket.txt", "w")
        f.write("")
        f.close()

    def get_ticket_number(self):
        my_ticket_num = r.choice(self.create_a_list())
        return my_ticket_num

    def assign_ticket(self, ti):
        with open('ticket.txt', 'r') as fp:
            for line in fp:
                x = line[:-1]
                if int(x) == ti:
                    del(x)
                    continue
                tick_list.append(x)
        return tick_list




    def return_ticket(self, ticket_nu):
        with open('ticket.txt', 'w') as fp:
           fp.write(ticket_nu)
        tick_list.append(ticket_nu)
        self.list_to_text(tick_list)

t = ticket()


