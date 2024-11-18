import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from DB.custumer_data import MyHotelDataList
from EDITED_TEXT import text as my_text

class Admin_class:
    # Room properties
    total_rooms = 10                                       
    occupied_rooms = 0                                         
    advance_rooms = 0                                          
    available_rooms = total_rooms - (occupied_rooms + advance_rooms)        
    
    total_money_received = 0

    cost_of_room = 1200                                     
    cost_of_advance_room = int(cost_of_room + (30 * cost_of_room) / 100) 

    def __init__(self, admin_name, admin_pass):
        self.admin_name = admin_name
        self.admin_pass = admin_pass

    def calculate_room_status(self):
        # 'This method is used to calculate status of Room number'
        self.occupied_rooms = sum(1 for customer in MyHotelDataList if customer['Room Status'].casefold() == 'book'.casefold())
        self.advance_rooms = sum(1 for customer in MyHotelDataList if customer['Room Status'].casefold() == 'advance'.casefold())
        self.available_rooms = self.total_rooms - (self.occupied_rooms + self.advance_rooms)
        
        return self.available_rooms, self.occupied_rooms, self.advance_rooms
    def passConfirmation(self):
        EnterPass=(input(my_text.colored_text('To isi baat pe **PASSWORD** btao phir---',"yellow")))
        return EnterPass
    def greeting(self):
        print(my_text.colored_text(my_text.heading(f"Welcome Administrator {self.admin_name}"), "yellow"))
        print(my_text.colored_text(my_text.heading("System Initialization in Progress..."), "yellow"))
    def optionForself(self):
        print(my_text.colored_bg_text(my_text.heading("Administrator Menu"), "blue"))
        print(my_text.heading("Please select an option\n"))
        print(my_text.colored_text("Option A", "blue") + ": View Room Status             " + my_text.colored_text("(   Room Occupancy Details   )", "magenta"))
        print(my_text.colored_text("Option B", "blue") + ": View Customer Status         " + my_text.colored_text("(   Customer Information     )", "magenta"))
        print(my_text.colored_text("Option C", "blue") + ": View Financial Status        " + my_text.colored_text("(   Revenue Information      )", "magenta"))
        print(my_text.colored_text("Option D", "blue") + ": View Complete Database       " + my_text.colored_text("(   All Records              )", "magenta"))
        print(my_text.colored_text("Option O", "blue") + ": Show Available Options       " + my_text.colored_text("(   Help Menu                )", "magenta"))
        print(my_text.colored_text("Option X", "blue") + ": Exit System                  " + my_text.colored_text("(   Close Application        )", "magenta"))
    def ChooseOption(self):
        print(my_text.line_text())
        option = str(input(my_text.colored_text("Enter your option choice: ", "blue")))
        print(my_text.colored_text(my_text.heading("Processing Request..."), "yellow"))
        return option
    def optarationAfterChoosing(self):
        ChoosedOpt = self.ChooseOption()
    
        if ChoosedOpt.casefold() == 'x'.casefold():
            print(my_text.colored_bg_text(my_text.heading("ALERT: Your Terminal is Exiting"), "yellow"))
            print(my_text.heading("Goodbye!"))
            return "RESET"
        elif( ChoosedOpt.casefold() == 'a'.casefold()):             #A
            self.RoomStatus()
            self.optarationAfterChoosing()
        elif( ChoosedOpt.casefold() == 'b'.casefold() ):          #B
            self.customerStatus()
            self.optarationAfterChoosing()
        elif( ChoosedOpt.casefold() == 'c'.casefold() ):          #C
            self.paisa()
            self.optarationAfterChoosing()
        elif( ChoosedOpt.casefold() == 'd'.casefold() ):          #D
            for i in range(0,len(MyHotelDataList)):#iterate over my list>dict
                print(my_text.colored_bg_text(my_text.heading('Customer {}'.format(i+1)), "yellow"))
                for j in MyHotelDataList[i]:
                    print(my_text.colored_text(j, "yellow") + ': ' + my_text.colored_text(MyHotelDataList[i][j], "blue"))
            self.optarationAfterChoosing()
        elif( ChoosedOpt.casefold() == 'o'.casefold() ):          #
            print('\n>>>>--->>HERE__ARE__YOUR__OPTION__AGAIN!!')
            self.optionForself()
            self.optarationAfterChoosing()
        else:
            print(my_text.line_text())
            print(my_text.colored_bg_text(my_text.heading("[ERROR] Invalid response. Please select again."), "red"))  
            print(my_text.line_text())
            self.optionForself()
            self.optarationAfterChoosing()
    def RoomStatus(self):
        self.calculate_room_status()
        print(my_text.colored_bg_text(my_text.heading("Room Status Information"), "blue"))
        print(my_text.colored_text(f"Total Available Rooms: {my_text.colored_text(self.total_rooms,"blue")}", "yellow"))
        print(my_text.colored_text(f"Total Number of Booked Rooms: {my_text.colored_text(self.occupied_rooms,"blue")}", "yellow"))
        print(my_text.colored_text(f"Total Number of Advance Booked Rooms: {my_text.colored_text(self.advance_rooms,"blue")}", "yellow"))
        print(my_text.colored_text(f"Total Number of Empty Rooms: {my_text.colored_text(self.available_rooms,"blue")}", "yellow"))
        
    def customerStatus(self):
        '''Details of Customer from BOOKED and RESERVED'''
        
        print(my_text.colored_bg_text(my_text.heading("Customer Status Information"), "blue"))
        print(my_text.colored_text(my_text.heading("CUSTOMER DETAILS OF ALL WHO BOOKED ROOM"), "yellow"))
        for i in range(0,len(MyHotelDataList)):
            if( MyHotelDataList[i]['Room Status'].casefold() == 'book'.casefold() ):
                print('\n' + my_text.colored_text('CUSTOMER INDEX: ', 'white') + my_text.colored_text(f'{i}', 'blue'))
                print(my_text.colored_text('CUSTOMER NAME: ', 'white') + my_text.colored_text(f'{MyHotelDataList[i]["Name"]}', 'blue'))
                print(my_text.colored_text('CUSTOMER AGE: ', 'white') + my_text.colored_text(f'{MyHotelDataList[i]["Age"]}', 'blue'))
                print(my_text.colored_text('CONTACT NUMBER: ', 'white') + my_text.colored_text(f'{MyHotelDataList[i]["phone"]}', 'blue'))
                print(my_text.colored_text('DURATION: ', 'white') + my_text.colored_text(f'{MyHotelDataList[i]["Duration(Days)"]}', 'blue'))
                print(my_text.colored_text('TOTAL COST: ', 'white') + my_text.colored_text(f'{MyHotelDataList[i]["Total Cost"]}', 'blue'))
        print(my_text.colored_text(my_text.heading("CUSTOMER DETAILS OF ALL WHO ADVANCE BOOKED ROOM"), "yellow"))
        for j in range(0,len(MyHotelDataList)):
            if( MyHotelDataList[j]['Room Status'].casefold() == 'advance'.casefold() ):
                print('\n' + my_text.colored_text('CUSTOMER INDEX: ', 'white') + my_text.colored_text(f'{j}', 'blue'))
                print(my_text.colored_text('CUSTOMER NAME: ', 'white') + my_text.colored_text(f'{MyHotelDataList[j]["Name"]}', 'blue'))
                print(my_text.colored_text('CUSTOMER AGE: ', 'white') + my_text.colored_text(f'{MyHotelDataList[j]["Age"]}', 'blue'))
                print(my_text.colored_text('CUSTOMER CONTACT NUMBER: ', 'white') + my_text.colored_text(f'{MyHotelDataList[j]["phone"]}', 'blue'))
                print(my_text.colored_text('DURATION: ', 'white') + my_text.colored_text(f'{MyHotelDataList[j]["Duration(Days)"]}', 'blue'))
                print(my_text.colored_text('TOTAL COST: ', 'white') + my_text.colored_text(f'{MyHotelDataList[j]["Total Cost"]}', 'blue'))
    def paisa(self):
        self.calculate_room_status()
        self.TotalPaisa()
        print(my_text.colored_bg_text(my_text.heading("Financial Status Information"), "blue"))
        print(my_text.colored_text('Revenue from booked rooms: ', 'yellow') + my_text.colored_text('${} '.format(self.occupied_rooms * self.cost_of_room), 'blue') + my_text.colored_text('(Cost per day: ', 'yellow') + my_text.colored_text('${})'.format(self.cost_of_room), 'blue'))
        print(my_text.colored_text('Revenue from advance booked rooms: ', 'yellow') + my_text.colored_text('${} '.format(self.advance_rooms * self.cost_of_advance_room), 'blue') + my_text.colored_text('(Cost per day: ', 'yellow') + my_text.colored_text('${})'.format(self.cost_of_advance_room), 'blue'))
        total_revenue = (self.occupied_rooms * self.cost_of_room) + (self.advance_rooms * self.cost_of_advance_room)
        print(my_text.colored_bg_text(my_text.heading('Total revenue: ${}'.format(total_revenue)), "red"))
    def TotalPaisa(self):
        for i in range(0,len(MyHotelDataList)):
            self.total_money_received += int(MyHotelDataList[i]['Total Cost'])
            return

hotel_owner = Admin_class('DEEPAK',9899)
