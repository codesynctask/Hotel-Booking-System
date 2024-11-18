import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from MY_MODULE.custumer_data import MyHotelDataList
from MY_MODULE import text as my_text
from MY_MODULE.admin import hotel_owner

def run_hotel_room_system():
    from main import run_hotel_room_system as run_system
    run_system()


class Customer_class:
    def Customer_greeting(self):
        print(my_text.colored_text(my_text.heading("Welcome to Our Hotel"), "yellow"))
        print(my_text.colored_text(my_text.heading("System Initialization in Progress..."), "yellow"))

    def show_customer_options(self):
        print(my_text.colored_bg_text(my_text.heading("Customer Menu"), "blue"))
        print(my_text.colored_bg_text(my_text.heading("Please select an option"), "blue"))
        print(my_text.colored_text("Option A", "blue") + ": Book a Room                        " + my_text.colored_text("(New Booking)", "magenta"))
        print(my_text.colored_text("Option B", "blue") + ": View Room Details                  " + my_text.colored_text("(Booking Information)", "magenta"))
        print(my_text.colored_text("Option C", "blue") + ": View Room Rates                    " + my_text.colored_text("(Price Information)", "magenta"))
        print(my_text.colored_text("Option D", "blue") + ": Check Out                          " + my_text.colored_text("(Cancel Booking)", "magenta"))
        print(my_text.colored_text("Option O", "blue") + ": Show Available Options             " + my_text.colored_text("(Help Menu)", "magenta"))
        print(my_text.colored_text("Option X", "blue") + ": Exit System                        " + my_text.colored_text("(Close Application)", "magenta"))

    def choose_option(self):
        print(my_text.line_text())
        option = str(input(my_text.colored_text("Enter your option choice: ", "blue")))
        print(my_text.colored_text(my_text.heading("Processing Request..."), "yellow"))
        return option

    def process_option(self):
        chosen_option = self.choose_option()
        
        if chosen_option.casefold() == 'x'.casefold():
            print(my_text.colored_bg_text(my_text.heading("ALERT: System Exit Initiated"), "yellow"))
            print(my_text.heading("Thank you for using our service!"))
            return "RESET"
            
        elif chosen_option.casefold() == 'a'.casefold():
            self.add_new_booking()  
            self.process_option()
            
        elif chosen_option.casefold() == 'b'.casefold():
            print(my_text.colored_bg_text(my_text.heading("Room Details Lookup"), "blue"))
            customer_name = str(input(my_text.colored_text('Enter your name: ', 'blue')))
            self.show_customer_details(customer_name)
            self.process_option()
            
        elif chosen_option.casefold() == 'c'.casefold():
            print(my_text.colored_bg_text(my_text.heading("Current Room Rates"), "blue"))
            print(my_text.colored_text("Standard Room Rate (per day):", "yellow") + my_text.colored_text(f" ${hotel_owner.cost_of_room}", "blue"))
            print(my_text.colored_text("Advance Booking Rate (per day):", "yellow") + my_text.colored_text(f" ${hotel_owner.cost_of_advance_room}", "blue"))
            self.process_option()
            
        elif chosen_option.casefold() == 'd'.casefold():
            print(my_text.colored_bg_text(my_text.heading("Room Checkout Process"), "blue"))
            customer_name = input(my_text.colored_text('Enter your name: ', 'blue'))
            self.process_checkout(customer_name)
            self.process_option()
            
        elif chosen_option.casefold() == 'o'.casefold():
            print(my_text.colored_bg_text(my_text.heading("Available Options"), "blue"))
            self.show_customer_options()  
            self.process_option()
            
        else:
            print(my_text.line_text())
            print(my_text.colored_bg_text(my_text.heading("Invalid Option Selected"), "red"))
            print(my_text.colored_bg_text(my_text.heading("Please Try Again"), "red"))
            print(my_text.line_text())
            self.show_customer_options()
            self.process_option()

    def show_customer_details(self, customer_name):
        found = False
        for customer in MyHotelDataList:
            if customer['Name'].casefold() == customer_name.casefold():
                found = True
                print(my_text.colored_bg_text(my_text.heading("Customer Information"), "blue"))
                print(my_text.colored_text("Name:", "yellow") + my_text.colored_text(f" {customer['Name']}", "blue"))
                print(my_text.colored_text("Age:", "yellow") + my_text.colored_text(f" {customer['Age']}", "blue"))
                print(my_text.colored_text("Contact:", "yellow") + my_text.colored_text(f" {customer['phone']}", "blue"))
                print(my_text.colored_text("Room Status:", "yellow") + my_text.colored_text(f" {customer['Room Status']}", "blue"))
                break
                
        if not found:
            print(my_text.colored_bg_text(my_text.heading("No Customer Record Found"), "red"))

    def process_checkout(self, customer_name):
        found = False
        for i, customer in enumerate(MyHotelDataList):
            if customer['Name'].casefold() == customer_name.casefold():
                found = True
                print(my_text.colored_bg_text(my_text.heading("Current Booking Details"), "blue"))
                print(my_text.colored_text("Name:", "yellow") + my_text.colored_text(f" {customer['Name']}", "blue"))
                print(my_text.colored_text("Room Status:", "yellow") + my_text.colored_text(f" {customer['Room Status']}", "blue"))
                
                confirm = input(my_text.colored_text("Confirm checkout? (yes/no): ", "yellow"))
                if confirm.casefold() == 'yes'.casefold():
                    del MyHotelDataList[i]
                    print(my_text.colored_bg_text(my_text.heading("Checkout Successful"), "yellow"))
                    print(my_text.colored_text("Thank you for staying with us!", "yellow"))
                break
                
        if not found:
            print(my_text.colored_bg_text(my_text.heading("No Booking Found"), "red"))

    def add_new_booking(self):
        print(my_text.colored_bg_text(my_text.heading("New Booking Process"), "blue"))
        
        # Get customer details
        customer_name = input(my_text.colored_text("Enter your name : ", "blue"))
        
        try:
            customer_age = int(input(my_text.colored_text("Enter your age: ", "blue")))
            contact_number = input(my_text.colored_text("Enter your contact number: ", "blue"))
            stay_duration = int(input(my_text.colored_text("Enter number of days for stay: ", "blue")))
        except ValueError:
            print(my_text.colored_bg_text(my_text.heading("Invalid Input: Please enter numeric values where required"), "red"))
            return

        # Show booking options
        print(my_text.colored_bg_text(my_text.heading("Select Booking Type"), "blue"))
        print(my_text.colored_text("1. Standard Booking", "yellow") + my_text.colored_text(f" (${hotel_owner.cost_of_room} per day)", "blue"))
        print(my_text.colored_text("2. Advance Booking", "yellow") + my_text.colored_text(f" (${hotel_owner.cost_of_advance_room} per day)", "blue"))
        
        booking_type = input(my_text.colored_text("Enter booking type (1/2): ", "blue"))

        # Process booking based on type
        if booking_type == "1":
            total_cost = stay_duration * hotel_owner.cost_of_room
            room_status = "book"
        elif booking_type == "2":
            total_cost = stay_duration * hotel_owner.cost_of_advance_room
            room_status = "advance"
        else:
            print(my_text.colored_bg_text(my_text.heading("Invalid Booking Type Selected"), "red"))
            return

        # Show booking summary
        print(my_text.colored_bg_text(my_text.heading("Booking Summary"), "blue"))
        print(my_text.colored_text("Name:", "yellow") + my_text.colored_text(f" {customer_name}", "blue"))
        print(my_text.colored_text("Age:", "yellow") + my_text.colored_text(f" {customer_age}", "blue"))
        print(my_text.colored_text("Contact:", "yellow") + my_text.colored_text(f" {contact_number}", "blue"))
        print(my_text.colored_text("Duration:", "yellow") + my_text.colored_text(f" {stay_duration} days", "blue"))
        print(my_text.colored_text("Total Cost:", "yellow") + my_text.colored_text(f" ${total_cost}", "blue"))
        
        # Confirm  booKing
        confirm = input(my_text.colored_text("Confirm booking? (yes/no): ", "yellow"))
        
        if confirm.casefold() == "yes".casefold():
            # Adding to my hotel array db
            new_booking = {
                "Name": customer_name,
                "Age": customer_age,
                "phone": contact_number,
                "Duration(Days)": stay_duration,
                "Room Status": room_status,
                "Total Cost": total_cost
            }
            
            MyHotelDataList.append(new_booking)
            print(my_text.colored_bg_text(my_text.heading("Booking Confirmed Successfully"), "blue"))
            print(my_text.colored_text("Thank you for choosing our hotel!", "yellow"))
        else:
            print(my_text.colored_bg_text(my_text.heading("Booking Cancelled"), "yellow"))

customer = Customer_class()
# customer.process_option()
