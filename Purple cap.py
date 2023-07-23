import csv
import random
import matplotlib.pyplot as plt
import mysql.connector as sql
con=sql.connect(host='localhost',user='root',passwd='jarvis18',database='jarvis')
x=con.cursor()
def star():
    rows=5 
    for i in range(0, rows):
        for j in range(0, i + 1):
            print("*", end=' ')
    print("\r")    
star()
def pattern():
    rows = 5
    for i in range(rows + 1, 0, -1):
        for j in range(0, i - 1):
            print("*", end=' ')
        print(" ")
print("\nWelcome to Purple cap")
print("best services in the city")
print("We kick out the competition\n")
pattern()
ch='u'
while ch!='e':
    star()
    print("1.Enter 's' to schedule a service\n2.Enter 'u' for employee information")
    print("3.Enter 'c' to cancel a service\n4.Enter 'e' to to exit the site")
    pattern()
    ch=input("Enter your choice:\n")
    if ch=='u':
        e=1
        star()
        with open("Agency.csv") as file:
            k=csv.reader(file)
            s=str(input("enter username:\n"))
            t=str(input("enter the password:\n"))
            pattern()
            for a in k:
                if a[0]!='Name':
                   if a[1]==s and a[2]==t:
                       print("\nWelcome back",a[0],'\n')
                       ch1=1
                       e=0
                       while ch1!=9:
                           star()
                           print("\n1.Press 1 to enter employee information\n2.Press 2 to display all employee information")
                           print("3.Press 3 to search employee information by name")
                           print("4.Press 4 to search employee information by profession")
                           print("5.Press 5 to modify employee information\n6.Press 6 to remove employee information")
                           print("7.Press 7 to see details of the file\n8.Press 8 for pending services\n9.Press 9 to exit")
                           ch1=int(input("Enter next command:\n"))
                           pattern()
                           if ch1==1:
                               ch2='yes'
                               while ch2!='no':
                                   star()
                                   print("Enter employee information\n")
                                   v=input("enter name:")
                                   w=int(input("enter age:"))
                                   u=str(input("enter profession:"))
                                   u=u.upper()
                                   y=str(input("enter days of availability:"))
                                   y=y.upper()
                                   p=int(input("enter salary:"))
                                   j=int(input("Enter phone number:"))
                                   q='insert into employee values("{}","{}","{}","{}","{}","{}")'.format(v,w,u,y,p,j)
                                   x.execute(q)
                                   con.commit()
                                   ch2=input("more??")
                                   pattern()
                               print("records added")
                           elif ch1==2:
                               w='select * from employee'
                               x.execute(w)
                               a=x.fetchall()
                               for i in a:
                                   print('Name:',i[0])
                                   print('Age:',i[1])
                                   print('Profession:',i[2])
                                   print('Days of availability:',i[3])
                                   print('Salary:',i[4])
                                   print('Phone number:',i[5])
                                   print('\n')
                           elif ch1==3:
                               s=str(input("Enter employee name:"))
                               print('\n')
                               w="select * from employee where name='{}'".format(s)
                               x.execute(w)
                               b=x.fetchall()
                               if len(b)>0:
                                   for j in b:
                                       print('Name:',j[0])
                                       print('Age:',j[1])
                                       print('Profession:',j[2])
                                       print('Days of availability:',j[3])
                                       print('Salary:',j[4])
                                       print('Phone number:',j[5])
                                       print('\n')
                               else:
                                   star()
                                   print("Employee does not exist")
                                   star()
                           elif ch1==4:
                               s=str(input("Enter the profession:"))
                               print('\n')
                               w='select * from employee where Profession="{}"'.format(s)
                               x.execute(w)
                               b=x.fetchall()
                               if len(b)>0:
                                   for j in b:
                                       print('Name:',j[0])
                                       print('Age:',j[1])
                                       print('Profession:',j[2])
                                       print('Days of availability:',j[3])
                                       print('Salary:',j[4])
                                       print('Phone number:',j[5])
                                       print('\n')
                               else:
                                   star()
                                   print("No Employee of this profession")
                                   star()
                           elif ch1==5:
                               s=str(input("Enter Employee's name:"))
                               q='select * from employee where name="{}"'.format(s)
                               x.execute(q)
                               b=x.fetchall()
                               if len(b)>0:
                                   star()
                                   u=str(input("Enter new profession:"))
                                   u=u.upper()
                                   y=str(input("enter days of availability:"))
                                   y=y.upper()
                                   o=int(input("enter salary:"))
                                   j=int(input("Enter phone number:"))
                                   star()
                                   w='update employee set Profession="{}",Days_of_availability="{}",Salary="{}",Phone_no="{}" where name="{}"'.format(u,y,o,j,s)
                                   x.execute(w)
                                   con.commit()
                                   print("Employee information modified")
                               else:
                                   print("Employee does not exist")
                           elif ch1==6:
                               pattern()
                               s=str(input("Enter employee's name:"))
                               w='select * from employee where name="{}"'.format(s)
                               x.execute(w)
                               b=x.fetchall()
                               if len(b)>0:
                                   p='delete from employee where name="{}"'.format(s)
                                   x.execute(p)
                                   con.commit()
                                   print("Employee information removed")
                               else:
                                   print("Employee does not exist")
                           elif ch1==7:
                               count=0
                               z={}
                               sizes=[]
                               labels=[]
                               u=[]
                               explode=[]
                               w='select * from employee'
                               x.execute(w)
                               a=x.fetchall()
                               for b in a:
                                   labels.append(b[2])
                                   count=count+1
                               for i in labels:
                                   z[i]=labels.count(i)
                               for k in z:
                                   sizes.append(z[k])
                                   u.append(k)
                               max=sizes[0]
                               for j in sizes:
                                   if j>max:
                                       max=j
                               for y in sizes:
                                   if y==max:
                                       explode.append(0.2)
                                   else:
                                       explode.append(0.1)
                               plt.pie(sizes,explode=explode,labels=u,autopct='%1.1f%%', shadow=True, startangle=140)
                               plt.axis('equal')
                               plt.show()
                               print("Number of employees-",count)
                           elif ch1==8:
                               count=0
                               p=[]
                               w='select * from scheduled_services'
                               x.execute(w)
                               a=x.fetchall()
                               for b in a:
                                   count=count+1
                                   p.append(b[2])
                               z={}
                               for i in p:
                                   z[i]=p.count(i)
                                   plt.bar(i,z[i])
                               plt.xlabel('Service')
                               plt.ylabel('No of services required')
                               plt.title('Services required')
                               print("Number of pending services-",count)
                               plt.show()
                           elif ch1==9:
                               print("&&&&Thank you%%%%%")
                           else:
                               print("Wrong command!!\n")
            if e==1:
                print("\nWrong username or password!!!!!!\n")
    elif ch=='s':
        star()
        p=str(input("Enter your name:"))
        l=str(input("Enter address:"))
        z=int(input("Enter phone number:"))
        pattern()
        print('\n')
        add="select * from employee"
        x.execute(add)
        g=x.fetchall()
        for i in range(0,len(g)):
            print(i+1,g[i][2])
        zx=str(input("Enter your service:"))
        w='select * from employee,cost where employee.profession=cost.profession and employee.profession="{}"'.format(zx)
        x.execute(w)
        a=x.fetchall()
        if len(a)>0:
            h=a[random.randint(0,len(a)-1)]
            print('\n')
            print("Service is available on the days-",h[3])
            y=input("Enter 'y' to schedule or 'n' to exit:")
            if y=='y':
                b=h[3].split(',')
                for i in range(0,len(b)):
                    print("Press",i+1,'for',b[i])
                q=int(input("Enter the choice:"))
                if (q-1)<len(b):
                    print("\nModes of payment available are:\n")
                    print("1.Online transaction via credit card\n2.Paypal\n3.Paytm\n4.Google pay\n5.Cash")
                    n=['Online transaction','Paypal','Paytm','Google pay','Cash']
                    u=int(input("enter your choice:"))
                    m=n[u-1]
                    b[q-1]=b[q-1].upper()
                    print("\nYour services are scheduled for:",b[q-1])
                    zx=zx.upper()
                    print("Service:",zx)
                    print("Service person:",h[0])
                    print("Cost of service per hour:",h[7])
                    print("Phone number of person:",h[5])
                    print("Mode of payment:",m)
                    o=random.randint(10000,40000)
                    print("Customer code:",o,'\n')
                    v='insert into scheduled_services values("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")'.format(p,l,zx,b[q-1],z,h[0],h[5],h[7],m,o)
                    print("#####Thank you for choosing our services$$$$$$$\n")
                    x.execute(v)
                    con.commit()
                else:
                    print("Wrong service day!!\n")
            else:
                print("\nSorry Services unavailable\n")
        else:
            print("No service available:")
    elif ch=='c':
        pattern()
        s=str(input("Enter your name:"))
        w='select * from scheduled_services where name="{}"'.format(s)
        x.execute(w)
        p=x.fetchall()
        if len(p)>0:
            for i in p:
                print("\nService cancelled")
                print("Hope to see you next time")
                print("Refund amount:",i[7]*0.2)
                print('via:',i[8],'\n')
                z='delete from scheduled_services where name="{}"'.format(s)
                x.execute(z)
                con.commit()
        else:
            print("\nNo services scheduled under this name\n")
    else:
        if ch=='e':
            print("******Thank you for choosing our services******")
        else:
            print("Wrong command!!\n")
con.close()
