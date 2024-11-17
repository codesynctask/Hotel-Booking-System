# room status

# this is the data of **HOTEL CUSTOMER**
MyHotelDataList=[]
# adding some random customer for comparing purpuse
cust1=MyHotelDataList.append({
    'Name':str('PANKAJ'),
    'Age':int(16),
    'phone':int('0000'),
    'Room Status':'BOOK',
    'Duration(Days)':2,
    'Total Cost': '{}'.format(2400)
})
cust1=MyHotelDataList.append({
    'Name':str('MEGHRAJ'),
    'Age':int(20),
    'phone':int('0000'),
    'Room Status':str('BOOK'),
    'Duration(Days)':2,
    'Total Cost': '{}'.format(2400)
})
cust1=MyHotelDataList.append({
    'Name':str('AVINASH'),
    'Age':int(99),
    'phone':int('0000'),
    'Room Status':str('ADVANCE'),
    'Duration(Days)':3,
    'Total Cost': '{}'.format(1560*3)
})



# a.1 Class For ***ADMIN***----------------------------
class adminBoss:
    naam='DEEPAK' #<<<<<<<<<<<<<<<<<<<<<admin name!!
    # passKey=9899
    
    TotalKamra=10                                       #Total Room
    BharaRoom=0                                         #Number of Booked room
    RsrvRoom=0                                          #Advance room
    khhaliRoom=TotalKamra-(BharaRoom + RsrvRoom)        #Empty room
    
    totalMoneyReceived=0

    costOfRoom=1200                                     #cost of Room Booking
    costOfAdvRoom=int(costOfRoom + (30*costOfRoom)/100) #cost of advance Booking

    def calculate_room_status(self):
        # 'This method is used to calculate status of Room number'
        self.BharaRoom = sum(1 for customer in MyHotelDataList if customer['Room Status'] == 'BOOK')
        self.RsrvRoom = sum(1 for customer in MyHotelDataList if customer['Room Status'] == 'ADVANCE')
        self.khhaliRoom = self.TotalKamra - (self.BharaRoom + self.RsrvRoom)
        
        return self.khhaliRoom, self.BharaRoom, self.RsrvRoom
    def passConfirmation(self):
        # method defined  for passWord Confirmation
        BossPass=9899
        EnterPass=(input('\n~~~~>>>To isi baat pe **PASSWORD** btao phir---                                   >>'))
        return EnterPass
    def maalikAapAAgye(self):
        # Method defined for *GREETING* **ADMIN**
        print('>>>Great **ADMIN {}  SIR** For your Confirmation---)'.format(maalik.naam))
        print('>>>INITIATING YOUR SETUP---    \n')
    def optionForMaalik(self):
        # Method defined for *Showing Option* to Select for **ADMIN**
        print('>>>Please Let me know What you want SIR..---  ')
        print('>>>Choose from ****BELOW__ONLY****---  ')
        print('>>>>---Option **A** for *Room ka lekha Jokha bta?*                                 i.e ***ROOM STATUS*** ') #Room Status
        print('>>>>---Option **B** for *Customer logo ka lekha Jokha bta?*                        i.e ***CUSTOMER STATUS*** ')#customer Status
        print('>>>>---Option **C** for *Kitne Paise aa gye h. bta jaldi?*                         i.e ***MONEY STATUS*** ')#money Status
        print('>>>>---Option **D** for *mereKo DataList dikha. sabka naam k saath. bta jaldi?*    i.e ***SHOW LIST OF DATA*** ')#money Status
        print('>>>>---Option **O** for *Opttion kya kya h..?*                                     i.e ***SHOW OPTION***  ')#show option of MAALIK
        print('>>>>---Option **X** for *Kuchh ni janana mere ko..?*                               i.e ***CANCEL TERMINAL***  ')#cancel terminal
    def ChooseOption(self):
        # Methods defined for **INPUT OPTION**
        meraOption = str(input('\n++++>>>>Type Your ***OPTION HERE!! ADMIN SIR***____                              >>'))
        print('>>>INITIATING YOUR SETUP---')
        return meraOption
    def optarationAfterChoosing(self):
        ChoosedOpt = maalik.ChooseOption() #storing **INPUT VALUE** for Logic
    
        if( ChoosedOpt == 'A'):             #A
            self.RoomStatus()
            self.optarationAfterChoosing()
        elif( ChoosedOpt == 'B' ):          #B
            self.customerStatus()
            self.optarationAfterChoosing()
        elif( ChoosedOpt == 'C' ):          #C
            maalik.paisa()
            self.optarationAfterChoosing()
        elif( ChoosedOpt == 'D' ):          #C
            for i in range(0,len(MyHotelDataList)):#iterate over my list>dict
                print('\nCustomer {}'.format(i+1))
                for j in  MyHotelDataList[i]:
                    print(j,':',MyHotelDataList[i][j])
            self.optarationAfterChoosing()
        elif( ChoosedOpt == 'O' ):          #O
            print('\n>>>>--->>HERE__ARE__YOUR__OPTION__AGAIN!!')
            self.optionForMaalik()
            self.optarationAfterChoosing()
        elif( ChoosedOpt == 'X' ):          #X
            print('>>>Wait ..')
            print('>>>You selected OPTION for **RESET**')
            print('>>>                                                                              ___***JAI___SHREE___RAM***_^_')
            print('__________[***ALERTING__YOU:[Your Terminal is Reseted]***]__________')
            PooraHotel()
        else:
            print('\n\n------------------->>>>>>>[***RESPONSE___IS___ERROR!!***]<<<<<<--------------------------\n')  
            print('--------------------->>>>>>>[***SELECT__AGAIN***]<<<<<<----------------------------\n')  
            maalik.optionForMaalik()
            maalik.optarationAfterChoosing()
    def RoomStatus(self):
        #'yaha pe hisaab kitaab h room ka'
        # maalik.checkNumberForRoom()
        maalik.calculate_room_status()
        print('\n>>>>---->>>>SHOWING__RESULT__FOR__***__ROOM___STATUS__***__')
        print('>>>TOTAL Number of ***AVAILABLE ROOM*** in Our Hotel                                 : [  {}  ]---'.format(maalik.TotalKamra))
        print('>>>TOTAL Number of ***BOOKED ROOM*** in Our Hotel                                    : [  {}  ]---'.format(maalik.BharaRoom) )
        print('>>>TOTAL Number of ***ADVANCE BOOKED ROOM*** in Our Hotel                            : [  {}  ]---'.format(maalik.RsrvRoom))
        print('>>>TOTAL Number of ***EMPTY ROOM*** in Our Hotel                                     : [  {}  ]---'.format(maalik.khhaliRoom))
        
    def customerStatus(self):
        'yaha customer ka hisab kitab h i.e Details of Customer from BOOKED and RESERVED'  
        print('\n>>>>---->>>>SHOWING__RESULT__FOR ***CUSTOMER___STATUS***__')
        print('>>>--->>>>**CUSTOMER_DETAILS** OF__ALL_WHO ***BOOKED___ROOM*** ')
        for i in range(0,len(MyHotelDataList)):
            if( MyHotelDataList[i]['Room Status']== 'BOOK' ):
                print('\n>>--CUSTOMER INDEX                       : {}'.format(i))
                print('>>CUSTOMER NAME                          : {}'.format(MyHotelDataList[i]['Name']))
                print('>>CUSTOMER AGE                           : {}'.format(MyHotelDataList[i]['Age']))
                print('>>CUSTOMER CONTACT NUMBER                : {}'.format(MyHotelDataList[i]['phone']))
                print('>>DURATION                               : {}'.format(MyHotelDataList[i]['Duration(Days)']))
                print('>>TOTAL COST                             : {}'.format(MyHotelDataList[i]['Toal Cost']))
        print('\n>>>--->>>>**CUSTOMER_DETAILS** OF__ALL_WHO ***RESERVED___ROOM***')
        for j in range(0,len(MyHotelDataList)):
            if( MyHotelDataList[j]['Room Status']== 'ADVANCE' ):
                print('\n>>--CUSTOMER INDEX                       : {}'.format(i))
                print('>>CUSTOMER NAME                          : {}'.format(MyHotelDataList[j]['Name']))
                print('>>CUSTOMER AGE                           : {}'.format(MyHotelDataList[j]['Age']))
                print('>>CUSTOMER CONTACT NUMBER                : {}'.format(MyHotelDataList[j]['phone']))
                print('>>DURATION                               : {}'.format(MyHotelDataList[j]['Duration(Days)']))
                print('>>TOTAL COST                             : {}'.format(MyHotelDataList[j]['Toal Cost']))
    def paisa(self):
        'kitna rokda aaya'
        maalik.calculate_room_status()
        maalik.TotalPaisa()
        print('\n>>>>---->>>>Showing RESULT For ***MONEY___STATUS***----')
        print('>>>>--->>COST__OF__ROOM__BOOKING__PER__DAY                                         : >>>[${}]<<<<'.format(maalik.costOfRoom))
        print('>>>>---Money Received from BOOKED ROOM                                             : >>>[${}]<<<<'.format(maalik.BharaRoom*maalik.costOfRoom))
        print('>>>>--->>COST__OF__ADVANCE__ROOM__BOOKING__PER__DAY                                : >>>[${}]<<<<'.format(maalik.costOfAdvRoom))
        print('>>>>---Money Received from ADVANCE BOOKED ROOM                                     : >>>[${}]<<<<'.format(maalik.RsrvRoom*maalik.costOfAdvRoom))
        print('>>>>--->>>___T_O_T_A_L____M_O_N_E_Y___                                             : >>>[${}]<<<<'.format((maalik.BharaRoom*maalik.costOfRoom) + (maalik.RsrvRoom*maalik.costOfAdvRoom)))
        print('>>>>--->>>___T_O_T_A_L____E_A_R_N_I_N_G___                                         : >>>[${}]<<<<'.format((maalik.BharaRoom*maalik.costOfRoom) + (maalik.RsrvRoom*maalik.costOfAdvRoom)))
    def TotalPaisa(self):
        for i in range(0,len(MyHotelDataList)):
            maalik.totalMoneyReceived += int(MyHotelDataList[i]['Total Cost'])
            return

#a.2 Object Defining for ***ADMIN***
maalik=adminBoss()

# ----------------------------------------------------------------------------------------------------
# # b.2 object for cUSTOMER
class RoomLeneWalaClass:
    # '''this section class belongs to Customer itself '''
    def CustomerAapAAgye():
        print('\n>>>Thank You **SIR (user)** For your NAME---)')
        print('>>>INITIATING YOUR SETUP---    ')
    def optionForCustomer():
        print('>>>Please Let me know What you want SIR..---  ')
        print('\n>>>Choose from ****BELOW__ONLY****---  n')
        print('>>>>---Option **A** for *Mere Ko ROOM lene ka h...*                               i.e ***ROOM BOOKING*** ') #BOOK ROOM
        print('>>>>---Option **B** for *Mere ko Mere Room k bare me bta...?*                     i.e ***ROOM DETAILS*** ')#DETAILS OF MY ROOM
        print('>>>>---Option **C** for *Kitne Paise ka padega bhai.*                             i.e ***ROOM CHARGES PER DAY*** ')#ROOM COST
        print('>>>>---Option **D** for *Room chhorna h .*                                        i.e ***EXIT BOOKED ROOM*** ')#removing data from list
        print('>>>>---Option **O** for *Opttion kya kya h..?*                                    i.e ***SHOW OPTION***  ')#show option of MAALIK
        print('>>>>---Option **X** for *Kuchh ni janana mere ko..?*                              i.e ***CANCEL TERMINAL***  ')#cancel terminal
    def ChooseOptionForCust():
        # Methods defined for **INPUT OPTION**
        meraOption = str(input('\n++++>>>>Type Your ***OPTION HERE!! Customer SIR***____                            >>'))
        print('>>>INITIATING YOUR SETUP---')
        return meraOption
    def optarationAfterChoosing():
            ChoosedOptC = RoomLeneWalaClass.ChooseOptionForCust() #storing **INPUT VALUE** for Logic
            if( ChoosedOptC == 'A'):
                RoomLeneWalaClass.AddMyCustomer()
                RoomLeneWalaClass.optarationAfterChoosing()
            elif( ChoosedOptC == 'B' ):
                print('\n>>>>---->>>>Showing RESULT For ***CUSTOMER__ROOM__DETAILS***----')
                 #storing **INPUT VALUE** for Logic
                CustN = str(input('\n++++>>>>Type Your ***NAME HERE!! TO CHECK YOUR DATA IN OUR HOTEL***____          >>'))

                listMeAppend=[] #list for comparing len of **no data found in LOOP**
                def CustDetails():
                    for i in range(0,len(MyHotelDataList)):
                        if(MyHotelDataList[i]['Name'] != CustN):
                            listMeAppend.append(1)
                            continue
                        else:
                            if( MyHotelDataList[i]['Name'] == CustN ):
                                print('\n>>>>--->>>C H E C K I N G . . .')
                                print('>>>AS I can check from my **DATA**...')
                                print('>>>Here are your ***DETAILS*** :')
                                print('\nYour **NAME**                                                                     : {}'.format(MyHotelDataList[i]['Name']))
                                print('     **AGE**                                                                      : {}'.format(MyHotelDataList[i]['Age']))
                                print('     **CONTACT No.**                                                              : {}'.format(MyHotelDataList[i]['phone']))
                                print(' And **ROOM STATUS**                                                              : {}'.format(MyHotelDataList[i]['Room Status']))
                                print('>>> D.O.N.E')
                                if( MyHotelDataList[i]['Name'] == CustN ):
                                    break
                CustDetails()
                if(len(listMeAppend)==len(MyHotelDataList)):#check if cust name exist in my List
                    print('\n___________[***NO___DATA___FOUNDED_________OF__GIVEN__CUSTOMER***]_________\n')
                    RoomLeneWalaClass.optionForCustomer()
                RoomLeneWalaClass.optarationAfterChoosing()
                
            elif( ChoosedOptC == 'C' ):
                #Room charges for booking and adv booking
                print('\n>>>>---->>>>Showing RESULT For ***CURRENT  ROOM  CHARGES***----')
                print('\nCost of **BOOKING ROOM** Per Day is                                               : ${}'.format(maalik.costOfRoom) )
                print('Cost of **ADVANCE BOOKING ROOM** Per Day is                                       : ${}'.format(maalik.costOfAdvRoom) )
                RoomLeneWalaClass.optarationAfterChoosing()
            elif( ChoosedOptC == 'D' ):
                #leave booked room
                print('\n>>>>---->>>>Showing RESULT For ***CANCEL  MY  BOOKING***----')
                leavRoom = input('>>> What is Your **REGISTERED NAME**                                             >>')

                LeaveMeAppend=[] #list for comparing len of **no data found in LOOP**
                def CustDetails():
                    for i in range(0,len(MyHotelDataList)):
                        if(MyHotelDataList[i]['Name'] != leavRoom):
                            LeaveMeAppend.append(1)
                            continue
                        else:
                            if( MyHotelDataList[i]['Name'] == leavRoom ):
                                print('\n>>>>--->>>C H E C K I N G . . .')
                                print('>>>AS I can check from my **DATA**...')
                                print('>>>Here are your ***DETAILS*** :')
                                print('\nYour **NAME**                                                                     : {}'.format(MyHotelDataList[i]['Name']))
                                print('     **AGE**                                                                      : {}'.format(MyHotelDataList[i]['Age']))
                                print('     **CONTACT No.**                                                              : {}'.format(MyHotelDataList[i]['phone']))
                                print(' And **ROOM STATUS**                                                              : {}'.format(MyHotelDataList[i]['Room Status']))
                                print('\n>>> SO, You want to **CHECK OUT**')
                                print('         >>WE HAVE CLEARED YOUR DATA FROM OUR HOTEL DATA BASE<<')
                                print('>>> D.O.N.E')
                                if( MyHotelDataList[i]['Name'] == leavRoom ):
                                    del MyHotelDataList[i]
                                    RoomLeneWalaClass.optionForCustomer()
                                    RoomLeneWalaClass.optarationAfterChoosing()
                                    
                            elif(len(LeaveMeAppend)==len(MyHotelDataList)):#check if cust name exist in my List
                                print('\n___________[***NO___DATA___FOUNDED_________OF__GIVEN__CUSTOMER***]_________\n')
                                RoomLeneWalaClass.optionForCustomer()
                                RoomLeneWalaClass.optarationAfterChoosing()
                            else:
                                print('\n\n------------------->>>>>>>[***RESPONSE___IS___ERROR!!***]<<<<<<--------------------------')  
                                print('--------------------->>>>>>>[***SELECT__AGAIN***]<<<<<<----------------------------\n\n')  
                                RoomLeneWalaClass.optionForCustomer()
                                RoomLeneWalaClass.optarationAfterChoosing()
                CustDetails()
                if(len(LeaveMeAppend)==len(MyHotelDataList)):#check if cust name exist in my List
                    print('\n___________[***NO___DATA___FOUNDED_________OF__GIVEN__CUSTOMER***]_________\n')
                    RoomLeneWalaClass.optionForCustomer()
                    RoomLeneWalaClass.optarationAfterChoosing()
            elif( ChoosedOptC == 'O' ):
                RoomLeneWalaClass.optionForCustomer()
                RoomLeneWalaClass.optarationAfterChoosing()
            elif( ChoosedOptC == 'X' ):
                print('>>>Wait ..')
                print('>>>You selected OPTION for **RESET**')
                print('>>>___***JAI___SHREE___RAM***_^_')
                print('__________[***ALERTING     YOU***]__________')
                print('_________________________________________________________________________________________')
                PooraHotel()
            else:
                print('\n\n------------------->>>>>>>[***RESPONSE___IS___ERROR!!***]<<<<<<--------------------------')  
                print('--------------------->>>>>>>[***SELECT__AGAIN***]<<<<<<----------------------------\n\n')  
                RoomLeneWalaClass.optionForCustomer()
                RoomLeneWalaClass.optarationAfterChoosing()
    def AddMyCustomer():
        print('\n>>>>---->>>>Showing RESULT For ***BUYING___HOTEL___ROOM***----')
        print('\n>>>Choose from ****BELOW__ONLY****---  n')
        print('>>>>---Option **BOOK** for *Mere Ko ROOM BOOK krna h...*                          i.e ***BOOKING OF HOTEL ROOM*** ') #BOOK ROOM
        print('>>>>---Option **ADVANCE** for *Mere Ko ROOM ADVANCE me BOOK krna h...*            i.e ***ADVANCE BOOKING OF HOTEL ROOM*** ') #BOOK ROOM

        AdvOrBook=input('\n>>>>>>--->>>>**TYPE__[**BOOK___or___ADVANCE**]                                    >>')
        if(AdvOrBook == 'BOOK'):
            print('You Want to **________BOOK YOUR ROOM___________**')
            print('The Cost of **ROOM BOOKing** for Each Days                                        : ${}'.format(maalik.costOfRoom))
            print('Type **YES**                                                                      : **COUNTINUE BOOKING**')
            print('Type **NO**                                                                       : **DON"T COUNTINUE BOOKING** ')

            BookOrNot=input('\nDo you want to proceed **YES** or **NO** :                                        >>')
            if(BookOrNot =='YES'):
                print('>>>>--->>>Please Enter Your **DETAILS BELOW** to Continue---')
                CustNewName=(input('>>Enter Your ***NAME*** to Proceed...                                             :'))
                CustNewAge=(input('>>Enter Your ***AGE*** to Proceed...                                              :'))
                CustNewPhone=(input('>>Enter Your ***CONTACT NUMBER*** to Proceed...                                   :'))
                CustBookDays=(input('>>Enter ***FOR HOW MANY DAY*** You want to BOOK...                                :'))
                print('\n>>So, As per Your Above Details .....')
                print('>>The **TOTAL COST** of {} day                                                     : ${}'.format(CustBookDays,int(CustBookDays)*int(maalik.costOfRoom)))
                print('\n                                     >>>>>>>>>>[YOUR__ROOM__HAS__BEEN__BOOKED]<<<<<<<<<<')
                print('                                                  >>[___Thank_____You___}<<')
                RoomLeneWalaClass.optionForCustomer()
                # appending Dat to list
                
                cust={                  #appending New Customer to List
                        'Name':CustNewName,
                        'Age':CustNewAge,
                        'phone':CustNewPhone,
                        'Room Status':'BOOK',
                        'Duration(Days)':CustBookDays,
                        'Toal Cost':'${}'.format(int(CustBookDays)*int(maalik.costOfRoom))
                    }
                MyHotelDataList.append(cust)
                return cust 
            elif(BookOrNot =='NO'):
                print('>>>OKAY, You dont want to continue with Booking Room.....')
                RoomLeneWalaClass.optionForCustomer()
                RoomLeneWalaClass.optarationAfterChoosing()
            else:
                print('------------------->>>>>>>[***RESPONSE___IS___ERROR!!***]<<<<<<--------------------------\n')  
                print('>>>-->>>Seems Like You dont want to Proceed with Booking Room..')
                print('--------------------->>>>>>>[***SELECT__AGAIN***]<<<<<<----------------------------\n')  
                RoomLeneWalaClass.optionForCustomer()
                RoomLeneWalaClass.optarationAfterChoosing()
                
        elif(AdvOrBook == 'ADVANCE'):

            print('You Want to **________ADVANE BOOK YOUR ROOM___________**')
            print('The Cost of **ROOM BOOKing** for Each Days :                                      : ${}'.format(maalik.costOfAdvRoom))
            print('Type **YES**                                                                      : **COUNTINUE ADVANCE BOOKING**')
            print('Type **NO**                                                                       : **DON"T COUNTINUE ADVANCE BOOKING** ')
            AdBookOrNot=input('Do you want to proceed **YES** or **NO** :                                        >>')
            if(AdBookOrNot =='YES'):
                print('>>>>Please Enter Your Details **BELOW** to Continue---')
                CustNewName=(input('>>Enter Your ***NAME*** to Proceed...'))
                CustNewAge=(input('>>Enter Your ***AGE*** to Proceed...'))
                CustNewPhone=(input('>>Enter Your ***CONTACT NUMBER*** to Proceed...'))
                CustBookDays=(input('>>Enter ***FOR HOW MANY DAY*** You want to BOOK...'))
                print('>>So, As per Your Details .....')
                print('>>The Total Cost of {} day                                                     : ${} '.format(CustBookDays,int(CustBookDays)*int(maalik.costOfAdvRoom)))
                print('\n                                     >>>>>>>>>>[YOUR__ADVANCR__ROOM__HAS__BEEN__BOOKED]<<<<<<<<<<')
                print('                                                  >>[___Thank_____You___}<<')
                RoomLeneWalaClass.optionForCustomer()
                # appending Dat to list
                cust={                  #appending New Customer to List
                        'Name':CustNewName,
                        'Age':CustNewAge,
                        'phone':CustNewPhone,
                        'Room Status':'ADVANCE',
                        'Duration(Days)':CustBookDays,
                        'Toal Cost':'${}'.format(int(CustBookDays)*int(maalik.costOfAdvRoom))
                    }
                MyHotelDataList.append(cust)
                return cust 
            elif(AdBookOrNot =='NO'):
                print('>>>OKAY, You dont want to continue with Advance Booking Room.....')
                RoomLeneWalaClass.optionForCustomer()
                RoomLeneWalaClass.optarationAfterChoosing()
            else:
                print('------------------->>>>>>>[***RESPONSE___IS___ERROR!!***]<<<<<<--------------------------\n')  
                print('>>>-->>>Seems Like You dont want to Proceed with Advance Booking Room..')
                print('--------------------->>>>>>>[***SELECT__AGAIN***]<<<<<<----------------------------\n')  
                RoomLeneWalaClass.optionForCustomer()
                RoomLeneWalaClass.optarationAfterChoosing()
        else:
            print('------------------->>>>>>>[***RESPONSE___IS___ERROR!!***]<<<<<<--------------------------')  
            print('Seems Like You dont want Hotel Room..')
            print('--------------------->>>>>>>[***SELECT__AGAIN***]<<<<<<----------------------------')  
            RoomLeneWalaClass.optionForCustomer()
            RoomLeneWalaClass.optarationAfterChoosing()
            
    
# ---------------------------logic of object execution

def PooraHotel():
    print('\n                                        ____________________________________________')  
    print('________________________________________>>>>>>>[***WELCOME__TO__OUR__HOTEL***]<<<<<<______________________________________________')  
    print('                                        ____________________________________________\n')  
    print('>>>>--->>>HOW__CAN__WE__HELP__YOU??')
    
    who = str(input('>>>>FIRSTLY, What is Your **NAME** Sir--->>>                                      >>'))
    
    if(who == maalik.naam):
        print('----Looks like, you are my **MAALIK**  :|    ')
        maalik.passConfirmation()
        maalik.maalikAapAAgye()
        maalik.optionForMaalik()
        maalik.optarationAfterChoosing()
        print('done')
    elif(who != maalik.naam):
        RoomLeneWalaClass.CustomerAapAAgye()
            # checking with loop **if cust already exist**
        for i in range(0,len(MyHotelDataList)):
            if( MyHotelDataList[i]['Name'] == who ):
                print('\nAS I can check from my data that...')
                print('YOU__ARE__ALREADY__AN__EXISTING__CUSTOMER:)\br')
                print('______[**HERE__ARE__YOUR__DETAILS**]______ :')
                print('Your **NAME** is                                                                  : {}'.format(MyHotelDataList[i]['Name']))
                print('     **AGE** is                                                                   : {}'.format(MyHotelDataList[i]['Age']))
                print('     **CONTACT-no.** is                                                           : {}'.format(MyHotelDataList[i]['phone']))
                print('And  **ROOM_STATUS** is                                                           : {}\n'.format(MyHotelDataList[i]['Room Status']))
                print('\nHow Can I help You {} Sir'.format(MyHotelDataList[i]['Name']))
        RoomLeneWalaClass.optionForCustomer()
        RoomLeneWalaClass.optarationAfterChoosing()
        print(MyHotelDataList)
    else:
        print('Aneesh Grover ki aavaaj me ...**Kya kr rah h tu**')  
        print('----------------------------Select Again-----------------------')
    
    
PooraHotel()
    
    
    
    
    


