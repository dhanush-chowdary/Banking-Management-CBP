
#Banking Management
import time
import re
import pymysql
from otp_verificaton import otp_validate
from greeting import greet
#Printing Welcome Message
opening_statement = "Welcome To Banking Management"
print("*************************************************")
print("       ",end="")
for d in opening_statement:
    time.sleep(0.1)
    print(d,end="")
print()
print("*************************************************")
print()

#Data Base Connectivity
conn = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database = "banking"
    )

#Menu Bar Code

while True:
    print("---- Choose Your Option ----")
    print("1. Account Creation")
    print("2. Deposit")
    print("3. Withdrawal")
    print("4. Mini Statement")
    print("5. Pin Generation")
    print("6. Get all Details")
    print("7. Change Pin")
    print("8. Send Greetings")
    print("9. Exit")
    print()
    try:
        option = int(input("Enter Your Option: "))
    except:
        print()
        print("Invalid Input - Give Integers")
        print()
    else:
        match (option):
            case 1:
                print()
                print("=== Account Creation ===")
                print()
                acc_num_pattern = r'\d{6}'
                #Take Account Number From the User
                for i in range(3):
                    acc_num = input("Enter Account Number: ")
                    res = re.fullmatch(acc_num_pattern,acc_num)
                    if res is not None:
                        acc_num = int(acc_num)
                        c1 = conn.cursor()
                        c1.execute("select * from accounts where acc_num = %s",(acc_num))
                        data = c1.fetchone()
                        if data is not None:
                            print()
                            print("Account Number already Exist - Try Agian")
                            print() 
                        else:
                            #Take Name From the User
                            name_pattern = r'[A-Za-z ]+'
                            for i in range(3):
                                name = input("Enter Your Name: ")
                                res = re.fullmatch(name_pattern,name)
                                if res is not None:
                                    break                                   
                                else:
                                    print()
                                    print("Invalid Name - Try Again")
                                    print()
                            
                            else:
                                print("Limit Exceeded")
                                break
                            #Taking Email From the User
                            email_pattern = r'^[a-z0-9]+@gmail.com$'
                            for i in range(3):
                                email = input("Enter Your Email: ")
                                res = re.fullmatch(email_pattern,email)
                                if res is not None:
                                    break
                                else:
                                    print()
                                    print("Invalid Email - Try Again")
                                    print()
                            else:
                                print("Limit Exceeded")
                                break
                            #Taking Balance From the User
                            balance = float(input("Enter Initial Balance: "))


                            #OTP Verification
                            result = otp_validate(email)
                            if result == False:
                                print()
                                print("OTP Verification Failed")
                                print()
                                break
                            else: 
                                c2 = conn.cursor()
                                c2.execute("insert into accounts values (%s,%s,%s,%s,%s)",(acc_num,name,email,balance,0))
                                conn.commit()
                                break

                    else:
                        print()
                        print("Invalid Format - Try Again")
                else:
                    print()
                    print("Chances are Exceeded")
                    print()
                print()
                print("== Account Created Successfully ==")
                print()
            case 2:
                print()
                print("=== Deposit ===")
                print()
                acc = int(input("Enter Account Number: "))
                c1 = conn.cursor()
                c1.execute("select * from accounts where acc_num = %s",(acc))
                data = c1.fetchone()
                if data is None:
                    print()
                    print("Account Number does not Exist")
                    print()
                else:
                    amt = float(input("Enter Amount to Deposit: "))
                    c2 = conn.cursor()
                    fa = data[3] + amt
                    c2.execute("update accounts set balance = %s where acc_num= %s",(fa,acc))
                    conn.commit()
                
                    print()
                    print("Amount Deposited Successfully")
                    print()
            case 3:
                print()
                print("=== Withdrawal ===")
                print()
                acc = int(input("Enter Account Number: "))
                c1 = conn.cursor()
                c1.execute("select * from accounts where acc_num = %s",(acc))
                data = c1.fetchone()
                if data is None:
                    print()
                    print("Account does not Exist")
                    print()
                elif data[-1] == 0: 
                    print()
                    print("Pin Not Generated")
                    print()
                else:
                    p = int(input("Enter Pin: "))
                    if p != data[-1]:  
                        print()
                        print("Invalid Pin - Try Again")
                        print()
                    else:
                        amt = float(input("Enter Amount: "))
                        if amt%5!=0:
                            print()
                            print("Invalid Amount Entered")
                            print()
                        else:
                            if amt > data[3]:
                                print()
                                print("Insufficient Funds")
                                print()
                            else:
                                c2 = conn.cursor()
                                fn = data[3] - amt
                                c1.execute("update accounts set balance = %s where acc_num = %s",(fn,acc))
                                conn.commit()
                                print()
                                print("Withdrawal Successfull")
                                print()         
            case 4:
                print()
                print("=== Mini Statement ===")
                print()
                acc_num_pattern = r'\d{6}'
                for i in range(3):
                    acc = input("Enter Account Number: ")
                    res = re.fullmatch(acc_num_pattern,acc)
                    if res is None:
                        print()
                        print("Invalid Account Number - Try again")
                        print()
                    else:
                        acc = int(acc)
                        c1 = conn.cursor()
                        c1.execute("select * from accounts where acc_num = %s",(acc))
                        data = c1.fetchone()
                        
                        if data is not None:
                            if data[-1] == 0:
                                print()
                                print("Pin Not Generated")
                                print()
                                break
                            else:
                                cpin_pattern = r'\d{4}'
                                
                                cpin = input("Enter Pin: ")
                                res = re.fullmatch(cpin_pattern,cpin)
                                if res is None:
                                    print()
                                    print("Invalid Pin format")
                                    print()
                                    break
                                else:
                                    cpin = int(cpin)
                                    if cpin != data[-1]:
                                        print()
                                        print("Invalid Pin")
                                        print()
                                        break
                                    else:
                                        print()
                                        print("-- Account Details --")
                                        print(f"Name: {data[1]}")
                                        print(f"Email: {data[2]}")
                                        print(f"Balance: {data[3]}")
                                        print()
                                        break
                        else:
                            print()
                            print("Acccount Does not Exist")
                            print()
                else:
                    print()
                    print("Limit Exceeded")
                    print()
            case 5:
                print()
                print("=== Pin Generation ===")
                print()

                acc = int(input("Enter Acccount Number: "))
                c1 = conn.cursor()
                c1.execute("select * from accounts where acc_num = %s",(acc))
                data = c1.fetchone()

                if data is None:
                    print()
                    print("Account Does not Exist")
                    print()
                else:
                    if data[-1] != 0:
                        print()
                        print("Pin Already Exist")
                        print()
                    else:
                        #OTP Verification
                        c3 = conn.cursor()
                        c3.execute("select email from accounts where acc_num = %s",(acc))
                        d = c3.fetchone()

                        result = otp_validate(d[0])
                        if result == False:
                            print()
                            print("OTP Verification Failed")
                            print()
                            break
                        else:
                            p = int(input("Enter Pin: "))
                            cp = int(input("Confirm Pin: "))
                            if p != cp:
                                print()
                                print("Pin Generation Failed")
                                print()
                            else:
                                c2 = conn.cursor()
                                c2.execute("update accounts set pin = %s where acc_num = %s",(p,acc))
                                conn.commit()
                                print()
                                print("Pin Generated Successfully")
                                print()
            case 6:
                uname = input("Enter Username: ")
                if uname != "admin":
                    print()
                    print("Incorrect User Name")
                    print()
                else:
                    pwd = input("Enter Password: ")
                    if pwd != "admin":
                        print()
                        print("In correct Password")
                        print()
                    else:   
                        f = open("details.txt","w")
                        f.write("Account Deatils of Users\n")
                        c1 = conn.cursor()
                        c1.execute("select * from accounts")
                        info = c1.fetchall()
                        for data in info:
                            f.write(f"\nAccount Number: {data[0]}\n")
                            f.write(f"Name: {data[1]}\n")
                            f.write(f"Email: {data[2]}\n")
                            f.write(f"Balance: {data[3]}\n")
                        f.close()
                        print()
                        print("Check the File")
                        print()
            case 7:
                print()
                print("=== Change Pin ===")
                print()
                
                acc = int(input("Enter Acccount Number: "))
                c1 = conn.cursor()
                c1.execute("select * from accounts where acc_num = %s",(acc))
                data = c1.fetchone()

                if data is None:
                    print()
                    print("Account Does not Exist")
                    print()
                elif data[-1] == 0:
                    print()
                    print("Pin Not Generated")
                    print()
                else:
                    op = int(input("Enter Old Pin: "))
                    if op != data[-1]:
                        print()
                        print("In Correct Pin")
                        print()
                    else:
                        np = int(input("Enter New Pin: "))
                        cnp = int(input("Re Enter New Pin: "))
                        if np != cnp:
                            print()
                            print("Pin Change Failed")
                            print()
                        else:
                            c2 = conn.cursor()
                            c2.execute("update accounts set pin = %s where acc_num = %s",(np,acc))
                            conn.commit()
                            print()
                            print("New Pin Updated")
                            print()
            case 8:
                print()
                print("=== Send Greetings ===")
                print()

                c = conn.cursor()
                c.execute("select name,email from accounts")
                data = c.fetchall()
                print(data)
                k = input("Enter Occation: ")

                for x in data:
                    greet(x[1],x[0],k)

                print()
                print("Emails Sent")
                print()
                
            case 9:
                print()
                print("************************")
                print("       Thank You")
                print("************************")
                print()
                break
            case _:
                print()
                print("=== Invalid Input - Try Again ===")
                print()
    
