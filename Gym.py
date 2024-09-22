import mysql.connector

print("""

--------------------------------------------
       WELCOME TO THE FITNESS ZONE
--------------------------------------------       
""")

mydb=mysql.connector.connect(host='localhost', user='root',password='1234')
mycursor=mydb.cursor()

#Creating database and tables
mycursor.execute("create database if not exists gym")
mycursor.execute("use gym")
mycursor.execute("""create table if not exists fees(Silver int, Gold int,
Platinum int)""")
mycursor.execute("""create table if not exists login(username varchar(25),
                   password varchar(10) not null)""")
mycursor.execute("""create table if not exists member(id int, name varchar(20),
                  gender varchar(10), category varchar(25), amount int)""")
mycursor.execute("create table if not exists sno(id int, did int)")
mycursor.execute("""create table if not exists trainer(id int(2), name varchar(30),
                 age int, gender varchar(10), salary int)""")
mydb.commit()

#inserting starting values
#for login
mycursor.execute("select * from login")
datacount=0
for i in mycursor:
    datatcount=1
if datacount==0:
    mycursor.execute("insert into login values('admin','1234')")
    mydb.commit
#for sno
datacount=0
mycursor.execute("select * from sno")
for i in mycursor:
    datatcount=1
if datacount==0:
    mycursor.execute("insert into sno values(0,0)")
    mydb.commit()
#for fees
datacount=0
mycursor.execute("select * from fees")
for i in mycursor:
    datatcount=1
if datacount==0:
    mycursor.execute("insert into fees values(1000,800,600)")
    mydb.commit()


#main body of the code

while True:
    print("""
1. LOGIN
2. EXIT          
        """ )
    choice=int(input("Enter your choice : "))
    if choice==1:
        password=input('Enter the password : ')
        mycursor.execute('select * from login')
        for i in mycursor:
            user,passs=i
        if passs==password:
            print("""
 __________________________________
|                                  |
|   1. Add Trainer                 |
|   2. Add Member                  | 
|   3. Remove Trainer              |
|   4. Remove Member               |
|   5. See All Trainers            |
|   6. See All Members             |
|   7. Modify existing records     |
|   8. Change Password             |
|   9. Go back                     |
|__________________________________|

""")
            choice=int(input('Enter your Choice : '))
            #Adding a trainer
            if choice==1:
                name=input("Enter the trainer's name : ")
                age=int(input('Enter the age : '))
                gender=input('Enter the gender : ')
                salary=int(input("Enter the salary : "))
                mycursor.execute("select * from sno")
                for i in mycursor:
                    t_id,t_did=i
                t_id=t_id+1
                mycursor.execute("insert into trainer values('"+str(t_id)+"','"+name+"','"+str(age)+"','"+gender+"','"+str(salary)+"')")
                mycursor.execute("update sno set id='"+str(t_id)+"'")
                mydb.commit()
                print("Trainer added successfully!")
            #Adding a member    
            elif choice==2:
                name=input("Enter the name of the member : ")
                gender=input("Enter the gender : ")
                print("""
 ________________________________________________________
|                                                        |
|    The available packages are :                        |
|    1. Silver ----- Amount -> 1000  [Per month 1000]    | 
|    2. Gold ------- Amount -> 2400 [Per month 800]      |
|    3. Platinum ---- Amount -> 3600 [Per month 600]     |
|________________________________________________________|

""")
                choice=input("Enter your choice : ")
                mycursor.execute("select * from fees")
                for i in mycursor:
                    t_s,t_g,t_p=i
                if choice=="1":
                    category='silver'
                    amount=t_s
                elif choice=="2":
                    category='gold'
                    amount=t_g
                elif choice=="3":
                    category='platinum'
                    amount=t_p
                else: 
                    print("Enter a valid choice")
                mycursor.execute("select * from sno")
                for i in mycursor:
                    i_id,i_did=i
                i_did=i_did+1
                mycursor.execute("insert into member values('"+str(i_did)+"','"+name+"','"+gender+"','"+category+"','"+str(amount)+"')")
                mycursor.execute("update sno set did='"+str(i_did)+"'")
                mydb.commit()
                print("Member Successfully Added!")

            #Removing a trainer    
            elif choice==3:
                idd=int(input("Enter the id of the trainer to remove : "))
                mycursor.execute("select * from trainer")
                flag=0
                for i in mycursor:
                    i_id=i[0]
                    if i_id==idd:
                        flag=1
                if flag==1:
                    mycursor.execute("delete from trainer where id='"+str(idd)+"'")
                    mydb.commit()
                    print("Removed Successfully!")
                else:
                    print("ID Not Found.")

            #Removing a member
            elif choice==4:
                idd=int(input("Enter the id of the member to be removed : "))
                mycursor.execute("select * from member")
                flag=0
                for i in mycursor:
                    t_id=i[0]
                    if t_id==idd:
                        flag=1
                if flag==1:
                    mycursor.execute("delete from member where id='"+str(idd)+"'")
                    mydb.commit()
                    print("Member removed successfully!")
                else:
                    print("ID Not Found")

            #Accessing All Trainers
            elif choice==5:
                trainers = "select * from trainer"
                cr1 = mydb.cursor()
                cr1.execute(trainers)
                res = list(cr1.fetchall())
                for row in res:
                    print(row)

            #Accessing All Members
            elif choice==6:
                members = "select * from member"
                cr2 = mydb.cursor()
                cr2.execute(members)
                res = list(cr2.fetchall())
                for row in res:
                    print(row)        

            #Modifying Information        
            elif choice==7:
                loop1='y'
                while loop1=='y':
                    print("""

 ________________________________
|                                |
|    1. Trainer Information      |
|    2. Member Information       |
|    3. Go back                  |
|________________________________|

""")
                    choice=int(input("Enter your choice : "))
                    
                    #Modifying trainer info
                    if choice==1:
                        idd=int(input("Enter id to be modified : "))
                        mycursor.execute("select * from trainer")
                        flag=0
                        for i in mycursor:
                            t_id=i[0]
                            if t_id==idd:
                                flag=1
                        if flag==1:
                            print("""
 __________________
|                  |
|    1. Name       |
|    2. Age        |
|    3. Gender     |
|    4. Salary     |
|__________________|

""")
                            ch=int(input("Enter your Choice : "))
                            if ch==1:
                                name=input("Enter the Name : ")
                                mycursor.execute("update trainer set name='"+name+"'where id='"+str(idd)+"'")
                                mydb.commit()
                                print("Updated successfully!")
                            elif ch==2:
                                age=int(input("Enter the Age : "))
                                mycursor.execute("update trainer set age='"+str(age)+"'where id='"+str(idd)+"'")
                                mydb.commit()
                                print("Updated successfully!")
                            elif ch==3:
                                gender=input("Enter the Gender : ")
                                mycursor.execute("update trainer set gender='"+gender+"'where id='"+str(idd)+"'")
                                mydb.commit()
                                print("Updated successfully!")
                            elif ch==4:
                                salary=int(input("Enter the Salary : "))
                                mycursor.execute("update trainer set salary='"+str(salary)+"'where id='"+str(idd)+"'")
                                mydb.commit()
                                print("Updated successfully!")
                            else:
                                print("Enter a valid choice : ")

                    #Modifying member info
                    elif choice==2:
                        idd=int(input("Enter ID of the member to modify : "))
                        mycursor.execute("select * from member")
                        flag=0
                        for i in mycursor:
                            t_id=i[0]
                            if t_id==idd:
                                flag=1
                        if flag==1:
                            print("""

 ___________________
|                   | 
|    1. Name        |
|    2. Age         |
|    3. Category    |
|___________________|

""")
                            ch2=int(input("Enter your choice : "))
                            if ch2==1:
                                name=input("Enter the Updated Name : ")
                                mycursor.execute("update member set name='"+name+"' where id='"+str(idd)+"'")
                                mydb.commit()
                                print("Successfully Updated!")
                            elif ch2==2:
                                gender=input("Enter the Updated Gender : ")
                                mycursor.execute("update member set gender='"+gender+"' where id='"+str(idd)+"'")
                                mydb.commit()
                                print("Successfully Updated!")
                            elif ch2==3:
                                print("""
 ___________________
|                   |
|   1. Silver       | 
|   2. Gold         |
|   3. Platinum     |
|___________________|

""")
                                mycursor.execute("select * from fees")
                                for i in mycursor:
                                    t_s,t_g,t_p=i
                                ch3=int(input("Enter your Choice : "))
                                if ch3==1:
                                    category="Silver"
                                    amt=t_s
                                elif ch3==2:
                                    category="gold"
                                    amt=t_g
                                elif ch3==3:
                                    category="platinum"
                                    amt=t_p
                                else:
                                    print("Enter a Valid Choice")
                                mycursor.execute("update member set category='"+category+"',amount='"+str(amt)+"' where id='"+str(idd)+"'")
                                mydb.commit()
                                print("Successfully Updated!")
                            else:
                                print("Enter a Valid Choice")
                        else:
                            print("ID Not Found")
                    elif choice==3:
                        break
                    else:
                        print("Invalid choice, Try again")

            #Changing Password    
            elif choice==8:
                passs=input("Enter the old Password : ")
                mycursor.execute("select * from login")
                for i in mycursor:
                    t_user,t_pass=i
                if t_pass==passs:
                    new_pass=input("Enter New Password : ")
                    mycursor.execute("update login set password='"+new_pass+"'")
                    mydb.commit()
                else:
                    print("Wrong Password, Try again")
                    
            elif choice==9:
                break
        else:
            print("Wrong password, Try Again")
    elif choice==2:
        break
    else:
        print('Enter a valid choice')
        
        
    
    
