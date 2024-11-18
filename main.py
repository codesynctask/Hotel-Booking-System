from DB.custumer_data import MyHotelDataList
from EDITED_TEXT import text as my_text
from CLASS.admin import Admin_class, hotel_owner
from CLASS.customer import Customer_class

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
        result = hotel_owner.optarationAfterChoosing()
        if result == "RESET":
            run_hotel_room_system()
        print('done')
    elif(who.casefold() != hotel_owner.admin_name.casefold() ) :
        Customer_class.Customer_gre()
            # checking with loop **if cust already exist**
        for i in range(0,len(MyHotelDataList)):
            if( MyHotelDataList[i]['Name'].casefold() == who.casefold() ):
                print('\nAS I can check from my data that...')
                print('YOU__ARE__ALREADY__AN__EXISTING__CUSTOMER:)\br')
                print('______[**HERE__ARE__YOUR__DETAILS**]______ :')
                print('Your **NAME** is                                                                  : {}'.format(MyHotelDataList[i]['Name']))
                print('     **AGE** is                                                                   : {}'.format(MyHotelDataList[i]['Age']))
                print('     **CONTACT-no.** is                                                           : {}'.format(MyHotelDataList[i]['phone']))
                print('And  **ROOM_STATUS** is                                                           : {}\n'.format(MyHotelDataList[i]['Room Status']))
                print('\nHow Can I help You {} Sir'.format(MyHotelDataList[i]['Name']))
        Customer_class.optionForCustomer()
        Customer_class.optarationAfterChoosing()
        print(MyHotelDataList)
    else:
        print('Aneesh Grover ki aavaaj me ...**Kya kr rah h tu**')  
        print('----------------------------Select Again-----------------------')
    
    
run_hotel_room_system()
    
    

