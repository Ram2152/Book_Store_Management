import mysql.connector
mydb=mysql.connector.connect (host="localhost", user="root", password="$Mrigeesh123")
#CREATING DATABASE AND TABLE
mycursor=mydb.cursor()
mycursor.execute("create database if not exists store")
mycursor.execute("use store")
mycursor.execute("create table if not exists signup(username varchar(20),password varchar(20))")
mycursor.execute("create table if not exists Available_Books(BookName varchar(30) primary key,Genre varchar(20),Quantity int,Author varchar(20),Publication varchar(30),Price int(4))")
mycursor.execute("create table if not exists Sell_rec(CustomerName varchar(20),PhoneNumber char(10) unique key, BookName varchar(30),Quantity int,Price int ,foreign key (BookName) references Available_Books(BookName))")
mycursor.execute("create table if not exists Staff_details(Name varchar(30), Gender varchar(10),Age int(3), PhoneNumber char(10) unique key , Address varchar(40))") 
def add():
    print("All information prompted are mandatory to be filled")
                    
    book=str(input("Enter Book Name:"))
    genre=str(input("Genre:"))
    quantity=int(input("Enter quantity:"))
    author=str(input("Enter author name:"))
    publication=str(input("Enter publication house:"))
    price=int(input("Enter the price:"))
    mycursor.execute("select * from Available_Books where bookname='"+book+"'")
    row=mycursor.fetchone()
    if row is not None:
        mycursor.execute("update Available_Books set quantity=quantity+'"+str(quantity)+"' where bookname='"+book+"'")
        mydb.commit()
        print("++++++++++++++++++++++\n++SUCCESSFULLY ADDED++\n++++++++++++++++++++++")
    else:
        mycursor.execute("insert into Available_Books(bookname,genre,quantity,author,publication,price) values('"+book+"','"+genre+"','"+str(quantity)+"','"+author+"','"+publication+"','"+str(price)+"')")
        mydb.commit()
        print("++++++++++++++++++++++\n++SUCCESSFULLY ADDED++\n++++++++++++++++++++++")
def sell():

    print("AVAILABLE BOOKS...""\n""(""book name"",""genre"",""number of copies"",""number of copies"",""author"",""publication house"",""price"")")
    mycursor.execute("select * from Available_Books ")
    for x in mycursor:
        print(x)
                      
    cusname=str(input("Enter customer name:"))
    phno=int(input("Enter phone number:"))
    book=str(input("Enter Book Name:"))
    price=int(input("Enter the price:"))
    n=int(input("Enter quantity:"))
    mycursor.execute("select quantity from available_books where bookname='"+book+"'")
    lk=mycursor.fetchone()
    if max(lk)<n:
        print(n,"Books are not available!!!!")
    else:
        mycursor.execute("select bookname from available_books where bookname='"+book+"'")
        log=mycursor.fetchone()
        if log is not None:
            mycursor.execute("insert into Sell_rec values('"+cusname+"','"+str(phno)+"','"+book+"','"+str(n)+"','"+str(price)+"')")
            mycursor.execute("update Available_Books set quantity=quantity-'"+str(n)+"' where BookName='"+book+"'")
            mydb.commit()
            print("++++++++++++++++++++++\n++BOOK HAS BEEN SOLD++\n++++++++++++++++++++++")
        else:
            print("BOOK IS NOT AVAILABLE!!!!!!!")
def search():
    print("""1:Search by name
2:Search by genre
3:Search by author""")
    l=int(input("Search by?:"))
    if l==1:
        bybookname()
    elif l==2:
        bygenre()
    elif l==3:
        byauthor()
    else:
        print("The chosen option is invalid")
    mydb.commit()    
def byauthor():
    au=input("Enter author to search:")
    mycursor.execute("select author from available_books where author='"+au+"'")
    home=mycursor.fetchall()
    if home is not None:
        print("++++++++++++++++++++\n++BOOK IS IN STOCK++\n++++++++++++++++++++")
        mycursor.execute("select * from available_books where author='"+au+"'")
        for z in mycursor:
            print(z)
    else:
        print("BOOKS OF THIS AUTHOR ARE NOT AVAILABLE!!!!!!!")
def bybookname():
    o=input("Enter Book to search:")
    mycursor.execute("select bookname from available_books where bookname='"+o+"'")
    tree=mycursor.fetchall()
    if tree is not None:
        print("++++++++++++++++++++\n++BOOK IS IN STOCK++\n++++++++++++++++++++")
        mycursor.execute("select * from available_books where bookname='"+o+"'")
        for a in mycursor:
            print(a)
    else:
        print("BOOK IS NOT IN STOCK!!!!!!!")
    mydb.commit()
def bygenre():
    
    g=input("Enter genre to search:")
    mycursor.execute("select genre from available_books where genre='"+g+"'")
    poll=mycursor.fetchall()
    if poll is not None:
         print("++++++++++++++++++++\n++BOOK IS IN STOCK++\n++++++++++++++++++++")
         mycursor.execute("select * from available_books where genre='"+g+"'")
         for y in mycursor:
             print(y)
    else:
        print("BOOKS OF SUCH GENRE ARE NOT AVAILABLE!!!!!!!!!")
def staffdet():
    print("1:New staff entry")
    print("2:Remove staff")
    print("3:Existing staff details")
    ch=int(input("Enter your choice:"))
    if ch==1:
        newstaff()
    elif ch==2:
        removestaff()
    elif ch==3:
        staffinfo()
def newstaff():
    fname=str(input("Enter Fullname:"))
    gender=str(input("Gender(M/F/O):"))
    age=int(input("Age:"))
    phno=int(input("Staff phone no.:"))
    add=str(input("Address:"))
    mycursor.execute("insert into Staff_details(name,gender,age,phonenumber,address) values('"+fname+"','"+gender+"','"+str(age)+"','"+str(phno)+"','"+add+"')")
    print("+++++++++++++++++++++++++++++\n+STAFF IS SUCCESSFULLY ADDED+\n+++++++++++++++++++++++++++++")
    mydb.commit()
def removestaff():
    nm=str(input("Enter staff name to remove:"))
    mycursor.execute("select name from staff_details where name='"+nm+"'")
    toy=mycursor.fetchone()
    if toy is not None:
        mycursor.execute("delete from staff_details where name='"+nm+"'")
        print("+++++++++++++++++++++++++++++++++\n++STAFF IS SUCCESSFULLY REMOVED++\n+++++++++++++++++++++++++++++++++")
        mydb.commit()
    else:
        print("STAFF DOESNOT EXIST!!!!!!")
def staffinfo():
    mycursor.execute("select * from Staff_details")
    run=mycursor.fetchone()
    print("(""name of staff"",""gender"",""age"",""phone number"",""address"")")
    for t in mycursor:
        print(t)
    if run is not None:
        print("EXISTING STAFF DETAILS...")
        for t in mycursor:
            print(t)
    else:
        print("NO STAFF EXISTS!!!!!!!")
    mydb.commit()
def sellhist():
    print("1:Sell history details")
    print("2:Reset Sell history")
    ty=int(input("Enter your choice:"))
    if ty==1:
        mycursor.execute("select * from sell_rec")
        for u in mycursor:
            
            print("(""customer"",""phone number"",""book sold"",""number of copies sold"",""selling price"")")
            print(u)
    if ty==2:
        bb=input("Are you sure(Y/N):")
        if bb=="Y":
            mycursor.execute("delete from sell_rec")
            mydb.commit()
        elif bb=="N":
            pass
def avlbooks():
    mycursor.execute("select * from available_books order by bookname")
    print("(""book name"",""genre"",""number of copies"",""number of copies"",""author"",""publication house"",""price"")")
    for v in mycursor:
        print(v)
      
def totinc():
    mycursor.execute("select sum(quantity*price) from sell_rec")
    for x in mycursor:
        l=list(x)
        print("THE TOTAL REVENUE IS",int(l[0]))
while True:
    print("1.SignUp\n2.Login")
    ch=int(input("SIGNUP/LOGIN(1,2):"))
#SIGNUP
    if ch==1:
        username=input("USERNAME:")
        pw=input("PASSWORD:")
        mycursor.execute("insert into signup values('"+username+"','"+pw+"')")
        mydb.commit()
#LOGIN
    elif ch==2:
            username=input("USERNAME:")
            mycursor.execute("select username from signup where username='"+username+"'")
            pot=mycursor.fetchone()
            if pot is not None:
                print("VALID USERNAME!!!!!!")
                pw=input("PASSWORD:")
                mycursor.execute("select password from signup where password='"+pw+"'")
                a=mycursor.fetchone()
                if a is not None:
                    print("+++++++++++++++++++++++\n+++LOGIN SUCCESSFULL+++\n+++++++++++++++++++++++")
                    print("=====================================================================\n++++++++++++++++++++++++++    MY BOOK STORE     +++++++++++++++++++++++++\n==========================================================================""")
                    while(True):
                        print("\n1:Add Books\n2:Sell Books\n3:Search Books\n4:Staff Details\n5:Sell History\n6:Available Books\n7:Total Income after the Latest Reset \n8:Logout")
                        a=int(input("Enter your choice:"))
                        if a==1:
                            add()
                        elif a==2:
                            sell()
                        elif a==3:
                            search()
                        elif a==4:
                            staffdet()
                        elif a==5:
                            sellhist()
                        elif a==6:
                            avlbooks()
                        elif a==7:
                            totinc()
                        elif a==8:
                            print("""YOU HAVE LOGGED OUT OF YOUR ACCOUNT.....COME BACK SOON :-)""")
                            break
                else:
                    print("++++++++++++++++++++++\n++INCORRECT PASSWORD++\n++++++++++++++++++++++")
            else:
                print("++++++++++++++++++++\n++INVALID USERNAME++\n++++++++++++++++++++")
    else:
        break
            
