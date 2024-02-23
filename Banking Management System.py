###----------------------------------------------------------------------------------------------------------------------------###
# ================================================================================================================================== #
# #####################################################-|--|--|-SOURCE CODE-|--|--|-################################################ #
# ================================================================================================================================== #
###----------------------------------------------------------------------------------------------------------------------------###
from datetime import date
import time
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

Setup = pd.read_csv('C://ProgramData//MySQL//MySQL Server 8.0//Uploads//Setup.csv', sep='=', header=None)
User = Setup.loc[0, 0]
Pwd = Setup.loc[0, 1]
Admn_Name = Setup.loc[0, 2]
Admn_Pwd = Setup.loc[0, 3]
Backup_Default = pd.read_csv('C://ProgramData//MySQL//MySQL Server 8.0//Uploads//Default_Backup_Location.csv', sep='=',header=None)


###----------------------------------------------------------------------------------------------------------------------------###
  ####################################### CREATING MYSQL DATABASE AND IMPORTING REQUIRED DATA ##################################
###----------------------------------------------------------------------------------------------------------------------------###
mydb = mysql.connector.connect(host="localhost", user=User, password=Pwd)
mycursor = mydb.cursor()
mycursor.execute("drop database if exists IP_Project")
mycursor.execute("create database IP_Project")
mycursor.execute('use IP_Project')
mycursor.execute("create table if not exists Admn_login(U_Name varchar(25) not null,PIN int not null)")
mycursor.execute("create table if not exists Accounts(S_No int,Name varchar(25) not null,Date_Of_Birth Date not null,Acc_no int primary key,Pan_Number varchar(10) not null,Residential_Address varchar(50) not null,Permanent_Address varchar(50) not null,Phone_No bigint not null,Branch_Name varchar(25) not null,Gender varchar(8) not null)")
mycursor.execute("create table if not exists Accnt_Pin(Acc_no int not null,PIN int(4) not null, FOREIGN KEY (ACC_No) REFERENCES Accounts(Acc_No))")
mycursor.execute("create table if not exists Accnt_Bal(Acc_No int not null,Acc_Balance bigint, FOREIGN KEY (Acc_No) REFERENCES Accounts(Acc_No))")
mycursor.execute("create table if not exists Money_Deposited(Transaction_Id varchar(12) not null,Acc_No int not null,Amount_Deposited float not null,Final_Balance float not null,Date date,Time varchar(15))")
mycursor.execute("create table if not exists Money_Withdrawed(Transaction_Id varchar(12) not null,Acc_No int not null,Amount_Withdrawed float not null,Final_Balance float not null,Date date,Time varchar(15))")
mycursor.execute("create table if not exists Money_Sent(Transaction_Id varchar(12) not null,Sender_Acc_No int not null,Receiver_Acc_No int not null,Amount float not null,Final_Balance float not null,Date date not null,Time varchar(15) not null,Foreign Key (Sender_Acc_No) references Accounts(Acc_No))")
mydb.commit()
mycursor.execute("alter table Money_Sent add foreign key (Receiver_Acc_No) references accounts(Acc_No)")
mycursor.execute('alter table accnt_bal alter column acc_balance set default 0')
mycursor.execute("alter table accounts alter column branch_name set default 'Haridwar'")
mycursor.execute('insert into admn_login values ("' + Admn_Name + '",' + str(Admn_Pwd) + ')')
mycursor.execute("load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Accounts.csv' into table Accounts fields terminated by '=' lines terminated by '\n'")
mycursor.execute("load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Accnt_PIN.csv' into table Accnt_PIN fields terminated by '=' lines terminated by '\n'")
mycursor.execute("load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Accnt_Bal.csv' into table Accnt_Bal fields terminated by '=' lines terminated by '\n'")
mycursor.execute("load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Money_Sent.csv' into table Money_Sent fields terminated by '=' lines terminated by '\n'")
mycursor.execute("load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Money_Deposited.csv' into table Money_Deposited fields terminated by '=' lines terminated by '\n'")
mycursor.execute("load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Money_Withdrawed.csv' into table Money_Withdrawed fields terminated by '=' lines terminated by '\n'")
mydb.commit()


###----------------------------------------------------------------------------------------------------------------------------###
  ######################################################## LOGIN PAGE ##########################################################
###----------------------------------------------------------------------------------------------------------------------------###
print('\n\n.......................................WELCOME TO OUR BANKING MANAGEMENT SYSTEM........................................',end='\n\n')
QQQ = 1
while QQQ == 1:
    time.sleep(2)
    Q = 1
    while Q == 1:
        print('Enter 1 For Admin Login', end='\n\n')
        print('Enter 2 For User Login', end='\n\n')
        print('Enter 3 To Close The Application', end='\n\n')
        A = int(input('Enter Your Choice : '))
        if A == 1:
            Q = 2
            KKK = 1
        elif A == 2:
            Q = 2
        elif A == 3:
            Q = 2
        else:
            print('Oops! Unexpected Input Entered', end='\n\n')
            time.sleep(2)
            print("Please Try Again", end='\n\n')
            time.sleep(2)
            Q = 1


    ###----------------------------------------------------------------------------------------------------------###
      ######################################### LOGIN AS AN ADMINISTRATOR ########################################
    ###----------------------------------------------------------------------------------------------------------###
    if A == 1:
        time.sleep(3)
        while KKK == 1:
            mycursor.execute('select * from Admn_login')
            ZX = mycursor.fetchall()
            U_Details = {}
            for (x, y) in ZX:
                U_Details[x] = y
            AA = 0
            while AA == 0:
                print('', end='\n')
                U = input('Enter Your User Name : ')
                if U not in U_Details.keys():
                    AA = 0
                    print('The User Name You Entered Is Wrong.', end='\n\n')
                    print('Please Try Again With A Valid User Name', end='\n\n')
                else:
                    AA = 1
            while AA == 1:
                print('', end='\n')
                P = input('Enter The Password Of The Corresponding User Name : ')
                if int(P) != U_Details[U]:
                    print('', end='\n')
                    print('The Password You Entered Is Incorrect', end='\n\n')
                    print('Please Try Again With The Correct Password', end='\n\n')
                    AA = 1
                else:
                    AA = 0
                    KKK = 2
        AA = 3
        while AA == 3:
            PPP = 1
            while PPP == 1:
                print('')
                print('From The List Below Select The Task You Want To Perform :-', end='\n\n')
                print('Enter 1 To Add Create A New Account', end='\n\n')
                print('Enter 2 To See Details Of All The Accounts', end='\n\n')
                print('Enter 3 To See The Details Of All The Transactions', end='\n\n')
                print('Enter 4 To Inspect The Account Balance Of All The Customers', end='\n\n')
                print('Enter 5 To Change The Default Backup Location', end='\n\n')
                print('Enter 6 To Backup Files', end='\n\n')
                print('Enter 7 To Return In The Main Menu', end='\n\n')
                M = int(input('Enter Your Choice : '))
                print('', end='\n')
                if M not in range(1, 8, 1):
                    print('Oops! Unexpected Input Entered', end='\n\n')
                    time.sleep(2)
                    print('Please Try Again', end='\n\n')
                    time.sleep(2)
                else:
                    PPP = 0

            #################### FOR CREATING A NEW ACCOUNT  ####################
            if M == 1:
                Name = str(input('Enter The Name Of The Account Holder : '))
                print('', end='\n')
                DOB = str(input('Enter The Date Of Birth [YYYY-MM-DD] : ', ))
                print('', end='\n')
                PAN_No = str(input('Enter The PAN Card No Of The Account Holder : '))
                print('', end='\n')
                Resd_Address = str(input("Enter Your Residential Address : "))
                print('', end='\n')
                Perm_Address = str(input("Enter Your Permanent Address : "))
                print('', end='\n')
                Branch = str(input('Enter The Name Of The Branch : '))
                print('', end='\n')
                Phone_No = str(int(input("Enter Your Phone Number : ")))
                print('', end='\n')
                GG = 1
                while GG == 1:
                    Gdr = str(input("Enter Your Gender [M/F] : "))
                    if Gdr not in ['M', 'm', 'F', 'f']:
                        print('', end='\n')
                        print("Oops! Unexpected Input Entered", end='\n\n')
                        time.sleep(2)
                        print("Please Try Again", end='\n\n')
                        time.sleep(2)
                    elif Gdr in ['M', 'm']:
                        Gender = 'Male'
                        GG = 2
                    elif Gdr in ['F', 'f']:
                        Gender = 'Female'
                        GG = 2
                mycursor.execute('select * from accounts')
                a = mycursor.fetchall()
                ZZ = 1
                if Branch == "":
                    Branch = 'Haridwar'
                for i in a:
                    ZZ += 1
                mycursor.execute("select Acc_No from accounts where Acc_No=(select max(Acc_No) from accounts)")
                HH = mycursor.fetchone()
                if str(HH) != 'None':
                    MM = HH[0] + 1
                else:
                    MM = 1104200401
                Account_No = str(MM)
                mycursor.execute('insert into accounts values ("' + str(ZZ) + '","' + Name + '","' + DOB + '",' + Account_No + ',"' + PAN_No + '","' + Resd_Address + '","' + Perm_Address + '","' + Phone_No + '","' + Branch + '","' + Gender + '")')
                mycursor.execute("insert into accnt_bal values ('" + Account_No + "',default)")
                mydb.commit()
                X = 1
                while X == 1:
                    print('', end='\n')
                    PIN = int(input("Enter Your Account's Pin Number : "))
                    print('', end='\n')
                    PIN2 = int(input("Confirm Your Account's Pin Number : "))
                    print('', end='\n')
                    if PIN != PIN2:
                        print('The Later PIN Number is Diffrent From The Former', end='\n\n')
                        time.sleep(2)
                        print('Please Try Again', end='\n\n')
                        time.sleep(2)
                    else:
                        mycursor.execute('insert into accnt_pin values ("' + Account_No + '","' + str(PIN) + '")')
                        mydb.commit()
                        time.sleep(1)
                        X = 2
                print('.............................Congratulations!..............................', end='\n\n')
                print('.................Your Account Has Been Successfully Created!.................', end='\n\n')
                time.sleep(3)
                print('....................Your Account Number Is', Account_No, '...................', end='\n\n')
                time.sleep(5)
                X = 8

            ############# FOR GETTING THE DETAILS OF ALL THE ACCOUNTS ##############
            elif M == 2:
                mycursor.execute("select S_No,Name,Acc_balance,Gender,PAN_Number,Date_Of_Birth,Residential_Address,Phone_No,Branch_Name from accounts join accnt_bal on accounts.Acc_no = accnt_bal.Acc_no;")
                a = mycursor.fetchall()
                a = pd.DataFrame(a, columns=['S_No', 'Name', 'Account Balance', 'Gender', 'PAN Number', 'Date Of Birth','Resd_Address', 'Phone_Number', 'Branch'])
                print('All The Accounts Opened In Our Bank Are As Follows : -', end='\n\n')
                a['Gender'] = a['Gender'].str.replace('\r', '')
                print(a.to_string(index=False), end='\n\n')
                time.sleep(3)

            ############## FOR GETTING DETAILS OF ALL THE TRANSACTIONS ###############
            elif M == 3:
                QW = 1
                while QW == 1:
                    print('From The List Below Select Your Choice : ', end='\n\n')
                    print('Enter 1 If You Want To See The Details Of Bank Deposits', end='\n\n')
                    print('Enter 2 If You Want To See The Details Of Bank Withdrawls', end='\n\n')
                    print('Enter 3 If You Want To See The Details Of Money Transfers', end='\n\n')
                    O = int(input('Enter Your Choice : '))
                    print('', end='\n')
                    if O == 1:
                        II = 'Bank Deposits'
                        QW = 0
                    elif O == 2:
                        II = 'Bank Withdrawls'
                        QW = 0
                    elif O == 3:
                        II = 'Money Transfers'
                        QW = 0
                    else:
                        print("Oops! Unexpected Input Entered", end='\n\n')
                        time.sleep(1)
                        print('Please Try Again', end='\n\n')
                        time.sleep(1)
                        QW = 1
                Num = int(input('Enter The Number Of Latest ' + str(II) + " That You Want To See : "))
                print('', end='\n')
                if O == 1:
                    mycursor.execute('select * from money_deposited order by transaction_id desc')
                    DB = mycursor.fetchall()
                    DB = pd.DataFrame(DB, columns=['Transacion Id', 'Account Number', 'Amount', 'Final Balance', 'Date','Time'])
                    print('The Latest ' + str(Num) + ' Bank Deposits Are As Follows :-', end='\n\n')
                    DB.columns.rename("S_No", inplace=True)
                    DB.index = range(1, int(len(DB) + 1))
                    DB['Time'] = DB['Time'].str.replace('\r', '')
                    print(DB.head(Num), end='\n\n')
                    time.sleep(4)
                elif O == 2:
                    mycursor.execute('select * from money_withdrawed order by transaction_id desc')
                    DB = mycursor.fetchall()
                    DB = pd.DataFrame(DB, columns=['Transacion Id', 'Account Number', 'Amount', 'Final Balance', 'Date','Time'])
                    DB.columns.rename("S_No", inplace=True)
                    DB.index = range(1, int(len(DB) + 1))
                    DB['Time'] = DB['Time'].str.replace('\r', '')
                    print('The Latest ' + str(Num) + ' Bank Withdrawls Are As Follows :-', end='\n\n')
                    print(DB.head(Num), end='\n\n')
                    time.sleep(4)
                elif O == 3:
                    mycursor.execute('select * from money_sent order by transaction_id desc')
                    DB = mycursor.fetchall()
                    DB = pd.DataFrame(DB,columns=['Transacion Id', "Sender's Account Number", "Receiver's Account Number",'Amount', 'Final Balance', 'Date', 'Time'])
                    DB.columns.rename("S_No", inplace=True)
                    DB.index = range(1, int(len(DB) + 1))
                    DB['Time'] = DB['Time'].str.replace('\r', '')
                    print('The Latest ' + str(Num) + ' Bank Transfers Are As Follows :-', end='\n\n')
                    DB.columns.rename("S_No", inplace=True)
                    print(DB.head(Num), end='\n\n')
                    time.sleep(4)

            ############ TO SHOW THE ACCOUNT BALANCE OF ALL THE CUSTOMERS ##############
            elif M == 4:
                mycursor.execute("select trim(acc_no) from accnt_bal;")
                a = mycursor.fetchall()
                a = pd.DataFrame(a)
                mycursor.execute("select acc_balance from accnt_bal;")
                b = mycursor.fetchall()
                b = pd.DataFrame(b)
                plt.bar(a[0], b[0], hatch='OX', edgecolor='silver', linewidth=2)
                plt.xlabel("Account Number")
                plt.ylabel("Account Balance In INR")
                plt.title("Account Balance Of All The Customers")
                plt.grid(True)
                plt.show()

            ################## TO CHANGE THE DEFAULT BACKUP FILES LOCATION #################
            elif M == 5:
                AK = 1
                while AK == 1:
                    DDD = input(str('Enter The New Default Location For Backup Files : '))
                    print('', end='\n\n')
                    AK = 2
                    while AK == 2:
                        print('The Location You Have Entered Is ' + DDD, end='\n\n')
                        CC = input(str('Confirm The New Default Location [Y/N] : '))
                        print('', end='\n')
                        if CC in ['Y', 'y']:
                            a = pd.DataFrame([DDD])
                            a.to_csv('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Default_Backup_Location.csv',
                                     index=None, header=None)
                            AK = 10
                            time.sleep(2)
                            print('The Default Location Of Backup Files Is Updated')
                        elif CC in ['n', 'N']:
                            AK = 1
                        else:
                            time.sleep(2)
                            print('Oops! Invalid Input Entered', end='\n\n')
                            print('Please Try Again', end='\n\n')
                            AK = 2

            ################################# TO BACKUP FILES ######################################
            elif M == 6:
                ALA = 1
                while ALA == 1:
                    ALA = 2
                    print('Enter 1 To Backup All The Files In The Default Location', end='\n\n')
                    print('Enter 2 To Backup Files In A Desired Location', end='\n\n')
                    print('Enter 3 To Return To Pevious Menu', end='\n\n')
                    ASD = str(input('Enter Your Choice : '))
                    print('')
                    if ASD == '1':
                        FFF = pd.read_csv('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Default_Backup_Location.csv',sep=',', header=None)
                        YYY = FFF.iloc[0, 0]
                        mycursor.execute("select * from accounts")
                        a = mycursor.fetchall()
                        a = pd.DataFrame(a, columns=['Serial Number', 'Name', 'Date Of Birth', 'Account Number','PAN Number', 'Residential Address', 'Permanent Address','Phone No', 'Branch Name', 'Gender'])
                        a['Gender'] = a['Gender'].str.replace('\r', '')
                        mycursor.execute("select * from accnt_bal")
                        b = mycursor.fetchall()
                        b = pd.DataFrame(b, columns=['Account Number', 'Account Balance'])
                        mycursor.execute("select * from accnt_pin")
                        c = mycursor.fetchall()
                        c = pd.DataFrame(c, columns=['Account Number', 'PIN'])
                        mycursor.execute("select * from money_sent")
                        d = mycursor.fetchall()
                        d = pd.DataFrame(d,columns=['Trnx ID', 'Sender Accnt Number', 'Receiver Accnt Balance', 'Ammount','Final Balance', 'Date', 'Time'])
                        d['Time'] = d['Time'].str.replace('\r', '')
                        mycursor.execute("select * from money_withdrawed")
                        e = mycursor.fetchall()
                        e = pd.DataFrame(e, columns=['Trnx ID', 'Account Number', 'Ammount', 'Final Balance', 'Date','Time'])
                        e['Time'] = e['Time'].str.replace('\r', '')
                        mycursor.execute("select * from money_deposited")
                        f = mycursor.fetchall()
                        f = pd.DataFrame(f, columns=['Trnx ID', 'Account Number', 'Ammount', 'Final Balance', 'Date','Time'])
                        f['Time'] = f['Time'].str.replace('\r', '')
                        g = pd.read_csv('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Default_Backup_Location.csv',header=None)
                        h = pd.DataFrame({'MySQL_Username': User, 'MySQL_Password': Pwd, 'Admn_Name': Admn_Name,'Admn_Pwd': Admn_Pwd}, index=[0])
                        a.to_csv(YYY + str('/Accounts.csv'), sep='=', index=None, header=None)
                        b.to_csv(YYY + str('/Accnt_Bal.csv'), sep='=', index=None, header=None)
                        c.to_csv(YYY + str('/Accnt_PIN.csv'), sep='=', index=None, header=None)
                        d.to_csv(YYY + str('/Money_Sent.csv'), sep='=', index=None, header=None)
                        e.to_csv(YYY + str('/Money_Withdrawed.csv'), sep='=', index=None, header=None)
                        f.to_csv(YYY + str('/Money_Deposited.csv'), sep='=', index=None, header=None)
                        g.to_csv(YYY + str('/Default_Backup_Location.csv'), sep='=', index=None, header=None)
                        h.to_csv(YYY + str('/Setup.csv'), sep='=', index=None, header=None)
                        print('Please Wait For Some Time', end='\n\n')
                        time.sleep(2)
                        print('The Backup Is Sucessfully Executed', end='\n\n')
                        time.sleep(2)
                    elif ASD == '2':
                        AK = 1
                        while AK == 1:
                            YYY = input(str("Enter The Location Where You Want To Store The Backup Files : "))
                            print('', end='\n\n')
                            QW = 0
                            while QW == 0:
                                print('The Location You Entered Is ' + YYY, end='\n\n')
                                CC = input(str('Confirm The Backup Location [Y/N] :'))
                                if CC in ['Y', 'y']:
                                    mycursor.execute("select * from accounts")
                                    a = mycursor.fetchall()
                                    a = pd.DataFrame(a, columns=['Serial Number', 'Name', 'Date Of Birth','Account Number', 'PAN Number', 'Residential Address','Permanent Address', 'Phone No', 'Branch Name','Gender'])
                                    a['Gender'] = a['Gender'].str.replace('\r', '')
                                    mycursor.execute("select * from accnt_bal")
                                    b = mycursor.fetchall()
                                    b = pd.DataFrame(b, columns=['Account Number', 'Account Balance'])
                                    mycursor.execute("select * from accnt_pin")
                                    c = mycursor.fetchall()
                                    c = pd.DataFrame(c, columns=['Account Number', 'PIN'])
                                    mycursor.execute("select * from money_sent")
                                    d = mycursor.fetchall()
                                    d = pd.DataFrame(d, columns=['Trnx ID', 'Sender Accnt Number','Receiver Accnt Balance', 'Ammount', 'Final Balance','Date', 'Time'])
                                    d['Time'] = d['Time'].str.replace('\r', '')
                                    mycursor.execute("select * from money_withdrawed")
                                    e = mycursor.fetchall()
                                    e = pd.DataFrame(e,columns=['Trnx ID', 'Account Number', 'Ammount', 'Final Balance','Date', 'Time'])
                                    e['Time'] = e['Time'].str.replace('\r', '')
                                    mycursor.execute("select * from money_deposited")
                                    f = mycursor.fetchall()
                                    f = pd.DataFrame(f,columns=['Trnx ID', 'Account Number', 'Ammount', 'Final Balance','Date', 'Time'])
                                    f['Time'] = f['Time'].str.replace('\r', '')
                                    g = pd.read_csv('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Default_Backup_Location.csv',header=None)
                                    a.to_csv(YYY + str('/Accounts.csv'), sep='=', index=None, header=None)
                                    b.to_csv(YYY + str('/Accnt_Bal.csv'), sep='=', index=None, header=None)
                                    c.to_csv(YYY + str('/Accnt_PIN.csv'), sep='=', index=None, header=None)
                                    d.to_csv(YYY + str('/Money_Sent.csv'), sep='=', index=None, header=None)
                                    e.to_csv(YYY + str('/Money_Withdrawed.csv'), sep='=', index=None, header=None)
                                    f.to_csv(YYY + str('/Money_Deposited.csv'), sep='=', index=None, header=None)
                                    g.to_csv(YYY + str('/Default_Backup_Location.csv'), sep='=', index=None,header=None)
                                    print('Please Wait For Some Time', end='\n\n')
                                    time.sleep(2)
                                    AK = 2
                                    QW = 1
                                    print('All The Files Are Succesfully Backed Up', end='\n\n')
                                elif CC in ['N', 'n']:
                                    AK = 2
                                    QW = 1
                                else:
                                    print('', end='\n\n')
                                    print("Oops! Invalid Input Entered", end='\n\n')
                                    print('Please Try Again', end='\n\n')
                                    QW = 0
                    elif ASD == '3':
                        time.sleep(2)
                    else:
                        print("Oops! Invalid Input Entered", end='\n\n')
                        print('Please Try Again', end='\n\n')
                        ALA = 1

            ######################## TO GO BACK TO LOGIN PAGE ########################
            elif M == 7:
                AA = 10
        ###----------------------------------------------------------------------------------------------------------------###
          ################################################ LOGIN AS A USER #################################################
        ###----------------------------------------------------------------------------------------------------------------###
    elif A == 2:
        KKK = 1
        while KKK == 1:
            mycursor.execute('select * from Accnt_pin')
            Q = mycursor.fetchall()
            Z = {}
            for (x, y) in Q:
                Z[x] = y
            AAA = 0
            while AAA == 0:
                print('', end='\n')
                U = int(input('Enter Your Account Number : '))
                if U not in Z.keys():
                    AAA = 0
                    print('', end='\n')
                    print('The Account Number You Entered Is Wrong.', end='\n\n')
                    time.sleep(1)
                    print('Please Try Again With A Valid Account Number', end='\n\n')
                    time.sleep(1)
                else:
                    AAA = 1
            while AAA == 1:
                print('', end='\n')
                P = int(input('Enter The Password Of The Corresponding Account : '))
                if P != Z[U]:
                    print('The Password You Entered Is Incorrect', end='\n\n')
                    print('Please Try Again With The Correct Password', end='\n\n')
                    time.sleep(1)
                    AAA = 1
                else:
                    AAA = 2
            print('', end='\n')
            print('...............Succesfully Logged In As A User ...............')
            time.sleep(1)
            MMM = 1
            while MMM == 1:
                print('')
                print('From The List Below Select The Task You Want To Perform :-', end='\n\n')
                print('Enter 1 To See Your User Profile', end='\n\n')
                print('Enter 2 To Check Your Account Balance', end='\n\n')
                print('Enter 3 To Modify Your Personal Details', end='\n\n')
                print('Enter 4 To Transter Money From Your Bank Account', end='\n\n')
                print('Enter 5 To See Your All Recent Transactions', end='\n\n')
                print('Enter 6 To Withdraw Money From Your Bank Account', end='\n\n')
                print('Enter 7 To Deposit Money In Your Bank Account', end='\n\n')
                print('Enter 8 To Delete Your Account', end='\n\n')
                print('Enter 9 If You Want To Login With An Another Account', end='\n\n')
                print('Enter 10 To Go Back', end='\n\n')
                I = int(input('Enter Your Choice : '))
                print('', end='\n')
                if I not in range(1, 11, 1):
                    print('Oops! Unexpected Input Entered', end='\n\n')
                    time.sleep(1)
                    print('Please Try Again', end='\n\n')
                    time.sleep(1)
                    MMM = 1

                ############# FOR DISPLAYING THE CUSTOMER'S DETAILS  ###############
                if I == 1:
                    print('', end='\n')
                    mycursor.execute('select name,date_of_birth,phone_no,pan_number,residential_Address,permanent_address,gender from accounts where Acc_No =' + str(U) + ';')
                    D = mycursor.fetchall()
                    D = pd.DataFrame(D, index=['Details'],columns=['Name', 'Date Of Birth', 'Phone No', 'PAN No', 'Residential Address','Permanent Address', 'Gender'])
                    D.columns.rename('Fields', inplace=True)
                    D['Gender'] = D['Gender'].str.replace('\r', '')
                    print('Your Details Are As Follows : ', end='\n\n')
                    print(D, end='\n\n')
                    time.sleep(3)

                ############# FOR DISPLAYING YOUR ACCOUNT BALANCE ##################
                elif I == 2:
                    mycursor.execute("select * from Accnt_Bal where Acc_No=" + str(U) + ";")
                    Bal = mycursor.fetchall()
                    SS = {}
                    for (x, y) in Bal:
                        SS[x] = y
                    print('', end='\n')
                    print('The Entered Account Number Is ' + str(U) + ' ', end='\n\n')
                    time.sleep(1)
                    print('Your Account Balance Is ₹' + str(SS[U]), end='\n\n')
                    time.sleep(3)

                ############# FOR MODIFYING THE CUSTOMER DETAILS  ###############
                elif I == 3:
                    VVV = 1
                    while VVV == 1:
                        print('', end='\n')
                        C = str(input("Do You Really Want To Make Changes In The Account Holder's Details [Y/N] : "))
                        if C in ['Y', 'y']:
                            ZZZ = 1
                            while ZZZ == 1:
                                print('', end='\n')
                                print('From The List Below Choose The Field For Modification ', end='\n\n')
                                print('Enter 1 To Modify The Name Of Account Holder', end='\n\n')
                                print('Enter 2 To Change The Phone Number Of The Account Holder', end='\n\n')
                                print('Enter 3 To Change Your Residential Address', end='\n\n')
                                print('Enter 4 To Modify Your Date Of Birth', end='\n\n')
                                MM = int(input('Enter Your Choice : '))
                                print('', end='\n')
                                if MM not in range(1, 5, 1):
                                    print('Oops! Unexpected Input Entered!', end='\n\n')
                                    time.sleep(1)
                                    print('Please Try Again', end='\n\n')
                                    time.sleep(1)
                                    ZZZ = 1
                                else:
                                    ZZZ = 7
                            if MM == 1:
                                name = str(input('Enter The New Name Of The Account Holder : '))
                                print('', end='\n')
                                mycursor.execute('update Accounts set Name="' + str(name) + '" where Acc_No=' + str(U) + ';')
                                print("The Account Holder's Name Has Been Modified", end='\n\n')
                                mydb.commit()
                                VVV = 2
                            elif MM == 2:
                                P_No = str(input('Enter The New Phone Number Of The Account Holder : '))
                                print('', end='\n')
                                mycursor.execute('update Accounts set Phone_No="' + str(P_No) + '" where Acc_No=' + str(U) + ';')
                                print("The Account Holder's Phone Number Has Been Modified", end='\n\n')
                                mydb.commit()
                                VVV = 2
                            elif MM == 3:
                                Resd_Address = str(input('Enter The New Residential Address Of The Account Holder : '))
                                print('', end='\n')
                                mycursor.execute('update Accounts set Residential_Address="' + Resd_Address + '" where Acc_No=' + str(U) + ';')
                                print("The Account Holder's Reisdential Address Has Been Modified", end='\n\n')
                                mydb.commit()
                                VVV = 2
                            elif MM == 4:
                                DOB = str(input('Enter The New Date Of Birth : '))
                                print('', end='\n')
                                mycursor.execute('update Accounts set Date_Of_Birth="' + DOB + '" where Acc_No=' + str(U) + ';')
                                print("The Account Holder's Date Of Birth Has Been Modified", end='\n\n')
                                mydb.commit()
                                VVV = 2
                            else:
                                print("Oops! Unexpected Input Entered", end='\n\n')
                                time.sleep(1)
                                print("Please Try Again", end='\n\n')
                                time.sleep(1)
                            time.sleep(3)

                        elif C in ['N', 'n']:
                            VVV = 9
                        else:
                            print("Oops! Unexpcted Input Entered", end='\n\n')
                            time.sleep(1)
                            print("Please Try Again", end='\n\n')
                            time.sleep(1)
                            VVV = 2

                ########### FOR TARNSFERING MONEY FROM YOUR BANK ACCOUNT ############
                elif I == 4:
                    DD = 1
                    print('', end='\n')
                    CC = str(input('Do You Really Want To Tansfer Money From Your Bank Account [Y/N] : '))
                    print('', end='\n')
                    if CC in ['Y', 'y']:
                        mycursor.execute('select * from accnt_bal')
                        Ao = mycursor.fetchall()
                        Acc = {}
                        for (x, y) in Ao:
                            Acc[x] = y
                        mycursor.execute('select * from Accnt_Bal where Acc_No=' + str(U) + ';')
                        AX = mycursor.fetchall()
                        Bal = {}
                        for (x, y) in AX:
                            Bal[x] = y
                        AZ = 1
                        while AZ == 1:
                            R_Acc_No = int(input('Enter The Account Number Of The Receiver : '))
                            print('', end='\n')
                            print('The Account Number You Entered Is ' + str(R_Acc_No) + '', end='\n\n')
                            if R_Acc_No not in Acc.keys():
                                print('The Account Number You Entered Is Invalid ', end='\n\n')
                                print('PLease Try Again', end='\n\n')
                                time.sleep(2)
                            elif R_Acc_No == int(U):
                                print("Oops! Both The Sender's And Receiver's Account Numbers Are Same", end='\n\n')
                                print("Please Try Again", end='\n\n')
                                time.sleep(2)
                            else:
                                AZ = 2
                        while AZ == 2:
                            AZ = 0
                            while AZ == 0:
                                Ammnt = int(input('Enter The Amount You Want To Transfer : '))
                                print('', end='\n')
                                if Ammnt > Bal[x]:
                                    print("Sorry! The Transaction Cannot Took Place", end='\n\n')
                                    print('Your Account Balance ₹' + str(Bal[x]) + ' Is Less Than The Amount To Be Transferred', end='\n\n')
                                    time.sleep(2)
                                    print('Please Enter An Appropriate Ammount Once Again', end='\n\n')
                                    time.sleep(1)
                                elif Ammnt == Bal[x]:
                                    print('You Want To Send Your All Money To The Other Account', end='\n\n')
                                    time.sleep(1)
                                    AZ = 2
                                else:
                                    print('You Want To Transfer ₹' + str(Ammnt) + ' To The Other Account', end='\n\n')
                                    time.sleep(1)
                                    AZ = 2
                            C = str(input('Confirm Your Choice [Y/N] : '))
                            print('', end='\n')
                            if C in ['N', 'n']:
                                AZ = 2
                            elif C in ['Y', 'y']:
                                print('..................Initiating Your Transaction..............', end='\n\n')
                                time.sleep(2)
                                print('...................Please Wait For Some Time...............', end='\n\n')
                                time.sleep(2)
                                Money_Left = str(Bal[x] - Ammnt)
                                mycursor.execute('Update Accnt_Bal set Acc_Balance=Acc_Balance+' + str(Ammnt) + ' where Acc_No=' + str(R_Acc_No) + ' ;')
                                mycursor.execute('Update Accnt_Bal set Acc_Balance=' + str(Money_Left) + ' where Acc_No=' + str(U) + ';')
                                mydb.commit()
                                Curr_Time = time.strftime("%H:%M:%S", time.localtime())
                                Date = date.today()
                                Initial = 'BTRNFR'
                                Final = 288411
                                mycursor.execute('select Date from money_sent')
                                KL = mycursor.fetchall()
                                for i in KL:
                                    Final += 1
                                Trnx_Id = str(str(Initial) + str(Final))
                                mycursor.execute(
                                    "insert into money_sent values ('" + Trnx_Id + "','" + str(U) + "','" + str(R_Acc_No) + "','" + str(Ammnt) + "','" + str(Money_Left) + "','" + str(Date) + "','" + str(Curr_Time) + "');")
                                mydb.commit()
                                print('..................Your Transaction Is Successfully Completed...................',end='\n\n')
                                time.sleep(2)
                                print('..........Succesfully Transfered ₹' + str(Ammnt) + ' From Your Bank Account........', end='\n\n')
                                time.sleep(2)
                                print('...........The Transaction Id For This Bank Transfer Is ' + Trnx_Id + '...........',end='\n\n')
                                time.sleep(3)
                                print('Your Remaining Account Balance Is ₹' + Money_Left, end='\n\n')
                                AZ = 3
                            else:
                                print('Oops! Unexpected Input Entered', end='\n\n')
                                time.sleep(1)
                                print('Please Try Again', end='\n\n')
                                time.sleep(1)
                                AZ = 2
                            time.sleep(3)
                    elif CC in ['n', 'N']:
                        MMM = 1
                    else:
                        print('Oops! Unexpected Input Entered', end='\n\n')
                        time.sleep(1)
                        print("Please Try Again", end='\n\n')
                        time.sleep(1)
                        MMM = 1
                    ############ FOR GETTING DETAILS OF ALL RECENT TRANSACTIONS ###########
                elif I == 5:
                    FRG = str(input('Enter The Date From Which You Want To Get Your Transactions [YYYY-MM-DD] : '))
                    print('', end='\n')
                    LRG = str(input('Enter The Date To Which You Want To Get Your Transactions [YYYY-MM-DD] : '))
                    print('', end='\n')
                    mycursor.execute('select * from money_deposited where date between "' + FRG + '" and "' + LRG + '" order by date,time;')
                    MD = mycursor.fetchall()
                    mycursor.execute('select * from money_withdrawed where date between "' + FRG + '" and "' + LRG + '" order by date,time;')
                    MW = mycursor.fetchall()
                    mycursor.execute('select * from money_sent where date between "' + FRG + '" and "' + LRG + '" order by date,time;')
                    MS = mycursor.fetchall()
                    MD = pd.DataFrame(MD, columns=['Transaction ID', 'Account No', 'Ammount Deposited', 'Final Balance','Date', 'Time'])
                    MD['Time'] = MD['Time'].str.replace('\r', '')
                    print("The Money Deposited In Your Account Is :- ", end='\n\n')
                    time.sleep(2)
                    print(MD[MD['Account No'] == int(U)].to_string(index=False), end='\n\n\n')
                    time.sleep(5)
                    MW = pd.DataFrame(MW,columns=['Transaction ID', 'Account No', 'Ammount Withdrawed', 'Final Balance','Date', 'Time'])
                    MW['Time'] = MW['Time'].str.replace('\r', '')
                    print("The Money Withdrawed From Your Account Is :- ", end='\n\n')
                    time.sleep(2)
                    print(MW[MW['Account No'] == int(U)].to_string(index=False), end='\n\n\n')
                    time.sleep(5)
                    MS = pd.DataFrame(MS, columns=['Transaction ID', "Sender's Acc. No", "Receiver's Acc. No",'Ammount Deposited', 'Final Balance', 'Date', 'Time'])
                    MS['Time'] = MS['Time'].str.replace('\r', '')
                    print("The Money Transferred From Your Account Is :- ", end='\n\n')
                    time.sleep(2)
                    print(MS[MS["Sender's Acc. No"] == int(U)].to_string(index=False), end='\n\n\n')
                    time.sleep(5)
                    MR = pd.DataFrame(MS, columns=['Transaction ID', "Sender's Acc. No", "Receiver's Acc. No",'Ammount Deposited', 'Final Balance', 'Date', 'Time'])
                    MR['Time'] = MR['Time'].str.replace('\r', '')
                    print("The Money Transferred To Your Account Is :- ", end='\n\n')
                    time.sleep(2)
                    print(MS[MS["Receiver's Acc. No"] == int(U)].to_string(index=False), end='\n\n\n')
                    time.sleep(5)

                ############## FOR WITHDRAW MONEY FROM YOUR BANK ACCOUNT ##############
                elif I == 6:
                    mycursor.execute('select * from Accnt_Bal where Acc_No=' + str(U) + ';')
                    AX = mycursor.fetchall()
                    Bal = {}
                    for (x, y) in AX:
                        Bal[x] = y
                        print('', end='\n')
                    print('Your Account Balance Is ₹' + str(Bal[x]), end='\n\n')
                    AZ = 0
                    while AZ == 0:
                        AZ = 1
                        while AZ == 1:
                            Money = int(input("Enter The Amount You Want To Withdraw From Your Account : "))
                            print('', end='\n')
                            if Money <= Bal[x]:
                                print('The Ammount You Want To Withdraw Is ₹' + str(Money), end='\n\n')
                                AZ = 0
                            elif Money > Bal[x]:
                                print('The Amount To Be Withdrawed ₹' + str(
                                    Money) + ' Is Greater Than Your Account Balance', end='\n\n')
                                print('Please Enter An Appropriate Amount And Try Again', end='\n\n')
                                AZ = 1
                            else:
                                print('Oops! Unexpected Input Entered', end='\n\n')
                                time.sleep(2)
                                print("Please Try Again", end='\n\n')
                                AZ = 1
                        C = str(input("Confirm Your Choice [Y/N] : "))
                        print('', end='\n')
                        if C in ["Y", "y"]:
                            print('..................Initiating Your Transaction..............', end='\n\n')
                            time.sleep(2)
                            print('...................Please Wait For Some Time...............', end='\n\n')
                            time.sleep(3)
                            Money_Left = str(Bal[x] - Money)
                            mycursor.execute('Update Accnt_Bal set Acc_Balance=' + Money_Left + ' where Acc_No=' + str(U) + ';')
                            Curr_Time = time.strftime("%H:%M:%S", time.localtime())
                            Date = date.today()
                            Initial = 'BKWDRL'
                            Final = 241405
                            mycursor.execute('select Date from money_withdrawed')
                            KL = mycursor.fetchall()
                            for i in KL:
                                Final += 1
                            Trnx_Id = str((Initial) + str(Final))
                            mycursor.execute("insert into money_withdrawed values ('" + Trnx_Id + "','" + str(U) + "','" + str(Money) + "','" + str(Money_Left) + "','" + str(Date) + "','" + str(Curr_Time) + "');")
                            mydb.commit()
                            print('..................Your Transaction Is Successfully Completed...................',end='\n\n')
                            time.sleep(2)
                            print('.......Succesfully Withrawed ₹' + str(Money) + ' From Your Bank Account......',end='\n\n')
                            time.sleep(2)
                            print('.........The transaction Id for This Withdrawl Is ' + Trnx_Id + '...........',end='\n\n')
                            print('..........Your Remaining Account Balance Is ₹' + Money_Left + '............',end='\n\n')
                            time.sleep(1)
                            AZ = 1
                            time.sleep(3)
                        elif C in ["N", 'n']:
                            AZ = 0
                        else:
                            print("Oops! Unexpected Input Entered", end='\n\n')
                            time.sleep(1)
                            print("Please Try Again", end='\n\n')
                            time.sleep(1)
                            AZ = 0

                ############## FOR DEPOSITING MONEY FROM YOUR BANK ACCOUNT ##############
                elif I == 7:
                    mycursor.execute('select * from Accnt_Bal where Acc_No=' + str(U) + ';')
                    AX = mycursor.fetchall()
                    Bal = {}
                    for (x, y) in AX:
                        Bal[x] = y
                    print('', end='\n')
                    print('Your Account Balance Is ₹' + str(Bal[x]), end='\n\n')
                    AZ = 0
                    while AZ == 0:
                        Money = int(input("Enter The Amount You Want To Deposit In Your Account : "))
                        print('', end='\n')
                        C = str(input("Confirm Your Choice [Y/N] : "))
                        print('', end='\n')
                        if C in ["Y", "y"]:
                            print('..................Initiating Your Transaction..............', end='\n\n')
                            time.sleep(1)
                            print('...................Please Wait For Some Time...............', end='\n\n')
                            time.sleep(2)
                            Total_Money = str(Bal[x] + Money)
                            mycursor.execute('Update Accnt_Bal set Acc_Balance=' + Total_Money + ' where Acc_No=' + str(U) + ';')
                            Curr_Time = time.strftime("%H:%M:%S", time.localtime())
                            Date = date.today()
                            Initial = 'BKDPST'
                            Final = 249401
                            mycursor.execute('select Date from money_deposited')
                            KL = mycursor.fetchall()
                            for i in KL:
                                Final += 1
                            Trnx_Id = str(str(Initial) + str(Final))
                            mycursor.execute("insert into money_deposited values ('" + Trnx_Id + "','" + str(U) + "','" + str(Money) + "','" + str(Total_Money) + "','" + str(Date) + "','" + str(Curr_Time) + "');")
                            mydb.commit()
                            print('..................Your Transaction Is Successfully Completed...................',end='\n\n')
                            time.sleep(1)
                            print('.........Succesfully Deposited ₹' + str(Money) + ' From Your Bank Account.........',end='\n\n')
                            print('............The transaction Id for This Deposite Is ' + Trnx_Id + '..............',end='\n\n')
                            print('...............Your Total Account Balance Is ₹' + Total_Money + '..................',end='\n\n')
                            time.sleep(1)
                            AZ = 1
                            time.sleep(3)
                        elif C in ["N", 'n']:
                            AZ = 0
                        else:
                            print("Oops! Unexpected Input Entered", end='\n\n')
                            time.sleep(1)
                            print("Please Try Again", end='\n\n')
                            time.sleep(1)
                            AZ = 0

                ################ FOR DELETING YOUR BANK ACCOUNT ##################
                elif I == 8:
                    print('', end='\n')
                    C = str(input("Do You Really Want To Delete Your Bank Account [Y/N] : "))
                    print('', end='\n')
                    if C in ['y', 'Y']:
                        mycursor.execute("delete from accnt_pin where Acc_No=" + str(U) + ";")
                        mycursor.execute("delete from accnt_bal where Acc_No=" + str(U) + ";")
                        mycursor.execute("delete from accounts where Acc_No=" + str(U) + ";")
                        mydb.commit()
                        print('............Your Account Is Succesfully Deleted.............', end='\n\n')
                        time.sleep(5)
                        MMM = 0
                        KKK = 0
                    elif C in ['N', 'n']:
                        MMM = 1
                    else:
                        print('Oops! Unexpected Input Entered ', end='\n\n')
                        time.sleep(1)
                        print('PLease Try Again')
                        time.sleep(1)
                        MMM = 1

                ################## FOR LOGIN WITH AN ANOTHER ACCOUNT ##################
                elif I == 9:
                    MMM = 0
                    KKK = 1
                    time.sleep(3)
                
                ####################### FOR GOING BACK IN PROGRAM #####################
                elif I == 10:
                    MMM = 0
                    KKK = 0
                    time.sleep(3)
    elif A == 3:
        QQQ = 6
print('', end='\n')

###----------------------------------------------------------------------------------------------------------------------------###
########################################### SAVING ALL THE DATA BACK IN DEFAULT LOCATION #####################################
###----------------------------------------------------------------------------------------------------------------------------###
print('Saving Essential Files Please Do Not Close The Application', end='\n\n')
mycursor.execute("select * from accounts")
a = mycursor.fetchall()
a = pd.DataFrame(a, columns=['Serial Number', 'Name', 'Date Of Birth', 'Account Number', 'PAN Number','Residential Address', 'Permanent Address', 'Phone No', 'Branch Name', 'Gender'])
a['Gender'] = a['Gender'].str.replace('\r', '')
mycursor.execute("select * from accnt_bal")
b = mycursor.fetchall()
b = pd.DataFrame(b, columns=['Account Number', 'Account Balance'])
mycursor.execute("select * from accnt_pin")
c = mycursor.fetchall()
c = pd.DataFrame(c, columns=['Account Number', 'PIN'])
mycursor.execute("select * from money_sent")
d = mycursor.fetchall()
d = pd.DataFrame(d, columns=['Trnx ID', 'Sender Accnt Number', 'Receiver Accnt Balance', 'Ammount', 'Final Balance','Date', 'Time'])
d['Time'] = d['Time'].str.replace('\r', '')
mycursor.execute("select * from money_withdrawed")
e = mycursor.fetchall()
e = pd.DataFrame(e, columns=['Trnx ID', 'Account Number', 'Ammount', 'Final Balance', 'Date', 'Time'])
e['Time'] = e['Time'].str.replace('\r', '')
mycursor.execute("select * from money_deposited")
f = mycursor.fetchall()
f = pd.DataFrame(f, columns=['Trnx ID', 'Account Number', 'Ammount', 'Final Balance', 'Date', 'Time'])
f['Time'] = f['Time'].str.replace('\r', '')
a.to_csv('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Accounts.csv', sep='=', index=None, header=None)
b.to_csv('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Accnt_Bal.csv', sep='=', index=None, header=None)
c.to_csv('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Accnt_PIN.csv', sep='=', index=None, header=None)
d.to_csv('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Money_Sent.csv', sep='=', index=None, header=None)
e.to_csv('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Money_Withdrawed.csv', sep='=', index=None, header=None)
f.to_csv('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Money_Deposited.csv', sep='=', index=None, header=None)
mycursor.execute("drop database IP_Project")
time.sleep(4)
print('Thank You For Using Our Services!', end='\n\n')
time.sleep(4)