import os
import time
import mysql.connector
import pandas as pd
def Retrieve_Backup(Y):
    a=pd.read_csv(Y+str('/Accounts.csv'),sep='=',header=None)
    b=pd.read_csv(Y+str('/Accnt_Bal.csv'),sep='=',header=None)
    c=pd.read_csv(Y+str('/Accnt_PIN.csv'),sep='=',header=None)
    d=pd.read_csv(Y+str('/Money_Sent.csv'),sep='=',header=None)
    e=pd.read_csv(Y+str('/Money_Withdrawed.csv'),sep='=',header=None)
    f=pd.read_csv(Y+str('/Money_Deposited.csv'),sep='=',header=None)
    g=pd.read_csv(Y+str('/Default_Backup_Location.csv'),sep='=',header=None)
    a.to_csv('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Accounts.csv',sep='=',index=None,header=None)
    b.to_csv('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Accnt_Bal.csv',sep='=',index=None,header=None)
    c.to_csv('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Accnt_PIN.csv',sep='=',index=None,header=None)
    d.to_csv('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Money_Sent.csv',sep='=',index=None,header=None)
    e.to_csv('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Money_Withdrawed.csv',sep='=',index=None,header=None)
    f.to_csv('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Money_Deposited.csv',sep='=',index=None,header=None)
    g.to_csv('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Default_Backup_Location.csv',sep='=',index=None,header=None)
AA=0
while AA==0:
    print('Enter 1 To Configure The Application',end='\n\n')
    print("Enter 2 To Change The Admin Password",end='\n\n')
    print('Enter 3 To Retrieve data From Backup Files',end='\n\n')
    time.sleep(3)
    C=input('Enter Your Choice : ')
    if C=='1':
        a=input("Do You Want To Configure The Program {Y/N} : ")
        if a in ['Y','y']:
            Path=input("Enter The Path Where You Want To Store The Application : ")
            time.sleep(2)
            Path=Path+'\Banking Management System'
            if not os.path.exists(Path):
                os.makedirs(Path)
            User=input("Enter The User In Which You Have Installed MySQL. Type 'root' For The Current User : ")
            time.sleep(2)
            Pwd=input("Please Enter The Password Of Your MySQL Server : ")
            time.sleep(2)
            Admn_Name=input("Enter The Name Of The Admin : ")
            time.sleep(2)
            Admn_Pwd=input("Enter The Password Of The Admin : ")
            time.sleep(2)
            Backup=Path+'\Final Banking Files Backup'
            Setup=pd.DataFrame({'MySQL_Username':User,'MySQL_Password':Pwd,'Admn_Name':Admn_Name,'Admn_Pwd':Admn_Pwd},index=[0])
            Setup.to_csv('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Setup.csv',sep='=',index=None,header=None)
            if not os.path.exists(Backup):
                os.makedirs(Backup)
            Default_Backup=pd.DataFrame([Backup],index=[0])
            Default_Backup.to_csv('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Default_Backup_Location.csv',sep='=',index=None,header=None)
            mydb=mysql.connector.connect(host="localhost",user=User,password=Pwd)
            if mydb.is_connected():
                print('',end='\n')
                BK=input("Do You Have Any Backup Of The Application {Y/N} : ")
                if BK in ['y','Y']:
                    Y=input(str("Enter The Location Where The Backup Files Are Stored : "))
                    print('',end='\n\n')
                    Retrieve_Backup(Y)
                    time.sleep(2)
                    print("The Application Is Ready To Use!")
                    AA=1
                elif BK in ['n','N']:
                    a=pd.DataFrame()
                    b=pd.DataFrame()
                    c=pd.DataFrame()
                    d=pd.DataFrame()
                    e=pd.DataFrame()
                    f=pd.DataFrame()
                    a.to_csv('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Accounts.csv',sep='=',index=None,header=None)
                    b.to_csv('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Accnt_Bal.csv',sep='=',index=None,header=None)
                    c.to_csv('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Accnt_PIN.csv',sep='=',index=None,header=None)
                    d.to_csv('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Money_Sent.csv',sep='=',index=None,header=None)
                    e.to_csv('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Money_Withdrawed.csv',sep='=',index=None,header=None)
                    f.to_csv('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Money_Deposited.csv',sep='=',index=None,header=None)
                    time.sleep(2)
                    print("The Application Is Ready To Use!")
                    AA=1
            else:
                print("Oops! The Connection Is Unsuccessful")
                time.sleep(2)
                print("Please Try Again!")
                time.sleep(3)
    elif C=='2':
        Setup=pd.read_csv('C://ProgramData//MySQL//MySQL Server 8.0//Uploads//Setup.csv',sep='=',header=None)
        Admn_Name=Setup.loc[0,2]
        Admn_Pwd=Setup.loc[0,3]
        User=Setup.loc[0,0]
        Pwd=Setup.loc[0,1]
        AS=0
        while AS==0:
            print('',end='\n')
            Name=input('Enter The Name Of The Admin : ')
            time.sleep(2)
            if Admn_Name==Name:
                print('',end='\n')
                Pswd=int(input('Enter The Prevoius Admin Password : '))
                time.sleep(2)
                if Admn_Pwd==Pswd:
                    print('',end='\n')
                    New_Pwd=input('Please Enter The New Password : ')
                    Admn_Pwd=New_Pwd
                    Setup=pd.DataFrame({'MySQL_Username':User,'MySQL_Password':Pwd,'Admn_Name':Admn_Name,'Admn_Pwd':Admn_Pwd},index=[0])
                    Setup.to_csv('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Setup.csv',sep='=',index=None,header=None)
                    print('',end='\n')
                    print("The Admin Password Is Sucessfully Changed!",end='\n\n')
                    AA=1
                    AS=1
                else:
                    print('Oops! You Entered The Wrong Password',end='\n\n')
                    time.sleep(2)
                    print('Please Try Again!',end='\n\n')
                    time.sleep(2)
            else:
                print('Oops! You Entered The Wrong Name',end='\n\n')
                time.sleep(2)
                print('Please Try Again!',end='\n\n')
                time.sleep(2)
                AS=1
    elif C=='3':
        Y=input(str("Enter The Location Where The Backup Files Are Stored : "))
        time.sleep(3)
        print('',end='\n\n')
        Retrieve_Backup(Y)
        print('Successfully Retrieved all The Data From The Backup Folder',end='\n\n')
    else:
        print("Oops! You Entered The Wrong Choice")
        time.sleep(2)
        print("Please Try Again!")
        time.sleep(2)
time.sleep(3)