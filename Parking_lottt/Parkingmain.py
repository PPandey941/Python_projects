
'''This is the executable file. you can type 500 for seeing the database and 1000 to clear the database.
'''
'''I am not able to delete the csv data after the customer has already checked out'''

import pandas as pd
import csv
from parkingticket import ticket
from parkingcustomer_data import customer
from parkingmoney import money

t = ticket()
t.list_to_text(t.create_a_list())
m = money()

while input != 100:
#We ask the user what they want to do park their car or take it out from parking.
    park_or_not = int(input("Type 1 to park your car \nType 2 for taking out your car"))

    print("\n")
#administrative access
    if park_or_not == 500:
        print("You have accessed the database")
        print(pd.read_csv('parkingcustomers.csv'))
    elif park_or_not == 1000:
        print("You have used the command to exit, the database will be cleared")
        f = open('parkingcustomers.csv', 'w')
        f.close()


    elif park_or_not == 1:
        c = customer()
        with open('parkingcustomers.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(c.header)
        c.add_content(c.data)



    elif park_or_not == 2:
        pf = pd.read_csv('parkingcustomers.csv')
        ticket_number = int(input("Enter your ticket number"))
        lo = pf[pf["ticket_no"] == str(ticket_number)]["time"]
        print(lo)
        entry_time = str(input("Enter the entry time"))
        exit_time = str(input("Enter in form of H:M"))
        mt = m.time_calulation(entry_time, exit_time)
        m.amount_to_pay(mt)
        ask_for_index = int(input("Enter the number beside your entry time"))
        pf.drop(labels= [ask_for_index,ask_for_index-1], axis=0, inplace=True)
        pf.to_csv("parkingcustomers.csv", index=False)
        payment = int(input("How would you like to pay? Type 1 for cash, Type 2 for credit and Type 3 for coupon"))
        if payment == 1:
            print("Thank you.Have a nice day.")
        elif payment == 2:
            input("Enter your credit card number")
            print("Thank you. Have a nice day")
        elif payment == 3:
            input("Type your coupon code")
            print("Thank You. Have a nice day")
        t.return_ticket(str(ticket_number))





    else:
        print("Wrong Input. Try Again!!!")



