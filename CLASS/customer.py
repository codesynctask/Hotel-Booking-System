import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from DB.custumer_data import MyHotelDataList
from EDITED_TEXT import text as my_text
from CLASS.admin import Admin_class , hotel_owner

def run_hotel_room_system():
    from main import run_hotel_room_system as run_system
    run_system()


class Customer_class:
    def Customer_greeting(self):
        print(my_text.colored_bg_text(my_text.heading('Thank you for providing your name.'), 'blue'))
        print(my_text.colored_text(my_text.heading('Initiating your setup...'), 'yellow'))
    def choose_option(self):
        print(my_text.line_text())
        option = str(input(my_text.colored_text("Enter your option choice: ", "blue")))
        print(my_text.colored_text(my_text.heading("Processing Request..."), "yellow"))
        return option
    def process_option(self):
        chosen_option = self.choose_option()
        
        if chosen_option.casefold() == 'x'.casefold():
            print(my_text.colored_bg_text(my_text.heading("ALERT: Your Terminal is Exiting"), "yellow"))
            print(my_text.heading("Goodbye!"))
            return "RESET"
            
        elif chosen_option.casefold() == 'a'.casefold():
            self.add_new_booking()  
            self.process_option()
            
        elif chosen_option.casefold() == 'b'.casefold():
            print(my_text.colored_bg_text(my_text.heading("Customer Room Details"), "blue"))
            customer_name = str(input(my_text.colored_text('Enter your name to check booking details: ', 'blue')))
            self.show_customer_details(customer_name)
            self.process_option()
            
        elif chosen_option.casefold() == 'c'.casefold():
            print(my_text.colored_bg_text(my_text.heading("Room Rate Information"), "blue"))
            print(my_text.colored_text(f"Standard Room Rate (per day): ${hotel_owner.cost_of_room}", "yellow"))
            print(my_text.colored_text(f"Advance Booking Rate (per day): ${hotel_owner.cost_of_advance_room}", "yellow"))
            self.process_option()
            
        elif chosen_option.casefold() == 'd'.casefold():
            print(my_text.colored_bg_text(my_text.heading("Room Checkout Process"), "blue"))
            customer_name = input(my_text.colored_text('Enter your registered name: ', 'blue'))
            self.process_checkout(customer_name)
            self.process_option()
            
        elif chosen_option.casefold() == 'o'.casefold():
            self.show_customer_options()  
            self.process_option()
            
        else:
            print(my_text.line_text())
            print(my_text.colored_bg_text(my_text.heading("[ERROR] Invalid response. Please select again."), "red"))
            print(my_text.line_text())
            self.show_customer_options()
            self.process_option()

    def show_customer_details(self, customer_name):
        found = False
        for customer in MyHotelDataList:
            if customer['Name'].casefold() == customer_name.casefold():
                found = True
                print(my_text.colored_bg_text(my_text.heading("Customer Information"), "blue"))
                print(my_text.colored_text("Name: ", "white") + my_text.colored_text(customer['Name'], "blue"))
                print(my_text.colored_text("Age: ", "white") + my_text.colored_text(customer['Age'], "blue"))
                print(my_text.colored_text("Contact: ", "white") + my_text.colored_text(customer['phone'], "blue"))
                print(my_text.colored_text("Room Status: ", "white") + my_text.colored_text(customer['Room Status'], "blue"))
                break
                
        if not found:
            print(my_text.colored_bg_text(my_text.heading("No Customer Record Found"), "red"))

    def process_checkout(self, customer_name):
        found = False
        for i, customer in enumerate(MyHotelDataList):
            if customer['Name'].casefold() == customer_name.casefold():
                found = True
                print(my_text.colored_bg_text(my_text.heading("Current Booking Details"), "blue"))
                print(my_text.colored_text("Name: ", "white") + my_text.colored_text(customer['Name'], "blue"))
                print(my_text.colored_text("Room Status: ", "white") + my_text.colored_text(customer['Room Status'], "blue"))
                
                confirm = input(my_text.colored_text("Confirm checkout? (yes/no): ", "yellow"))
                if confirm.casefold() == 'yes'.casefold():
                    del MyHotelDataList[i]
                    print(my_text.colored_bg_text(my_text.heading("Checkout Successful"), "blue"))
                break
                
        if not found:
            print(my_text.colored_bg_text(my_text.heading("No Booking Found"), "red"))

customer = Customer_class()
customer.process_option()
