from MY_MODULE.custumer_data import MyHotelDataList
from MY_MODULE import text as my_text
from MY_MODULE.admin import hotel_owner
from MY_MODULE.customer import customer

# ----------------------------------------------------------------------------------------------------

def run_hotel_room_system():
    print(my_text.line_text())
    print(my_text.colored_bg_text(my_text.heading("< WELOCME TO OUR HOTEl />"),"blue"))
    print(my_text.line_text())
    
    print(my_text.heading('HOW CAN WE HELP YOU?'))
    
    who = str(input('Who are you?\t:\t'))
    
    if(who.casefold() == hotel_owner.admin_name.casefold() ) :
        print(my_text.colored_text('Looks like, you are my OWNER 🤔', 'yellow'))
        hotel_owner.passConfirmation()
        hotel_owner.greeting()
        hotel_owner.optionForself()
        result = hotel_owner.optarationAfterChoosing() #option for owner already written🍵
        if result == "RESET":
            run_hotel_room_system()
        print('done Owner')
    elif(who.casefold() != hotel_owner.admin_name.casefold() ) :
        customer.Customer_greeting()
        for i in range(0,len(MyHotelDataList)):
            # checking with loop **if cust already exist**
            if( MyHotelDataList[i]['Name'].casefold() == who.casefold() ):
                print(my_text.colored_text('Existing Customer Details:', 'yellow'))
                print(my_text.colored_text('Name:', 'blue') + my_text.colored_text(MyHotelDataList[i]['Name'], 'magenta'))
                print(my_text.colored_text('Age:', 'blue') + my_text.colored_text(MyHotelDataList[i]['Age'], 'magenta'))
                print(my_text.colored_text('Contact:', 'blue') + my_text.colored_text(MyHotelDataList[i]['phone'], 'magenta'))
                print(my_text.colored_text('Room Status:', 'blue') + my_text.colored_text(MyHotelDataList[i]['Room Status'], 'magenta'))
                print(my_text.colored_text('How can I assist you, ', 'yellow') + my_text.colored_text(MyHotelDataList[i]['Name'], 'magenta') + '?')
        customer.show_customer_options()
        customer.choose_option()
        customer.process_option()
        print(my_text.colored_bg_text(MyHotelDataList, "white"))
    else:
        print(my_text.colored_text("Invalid input detected. Please try again.", "red"))
        print(my_text.colored_bg_text(my_text.heading("Please select a valid option"), "blue"))
    
    
run_hotel_room_system()
    
    

