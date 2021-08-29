class user:
    name=''
    group=''
    area=''
    cont=''

class admin:
    name=''
    adminid=''

def detail_user():
    user.name=input("please enter name: ")
    user.group=input("Please enter blood group: ")
    user.area=input("Please enter area number: ")
    user.cont=input("Please enter contact number: ")
    status=input("Donor[d] or recipient[r]: ")
    return status

def request():
    file=open('donors.txt','r')
    flag=0
    for line in file:
        if user.group in line:
            if user.area in line:
                flag=1
                print("The details of donor: ")
                print(line)
    file.close()
    if flag==0:
        print("No donor available")

def don():
    file=open('donors.txt','a')
    L=[user.name,'              ',user.group,
            '                ',user.area,'                  ',user.cont]
    file.writelines(L)
    file.close()

def rec():
    lvl=input("Is this an emergency?[y/n] ")
    if lvl=='y':
        request()
    elif lvl=='n':
        file=open('donors.txt','a')
        file.write("There is a request :")
        L=[user.name,'              ',user.group,
            '                ',user.area,'                  ',user.cont]
        file.writelines(L)
        file.close()
        print("Your request for blood has been entered")
    else: 
        print("Incorrect choice")

def use():
    b=detail_user()
    if b=='d':
        don()
    elif b=='r':
        rec()
    else:
        print("Invalid input")

#valid admin IDs are 1234, 5678, 9012, 3456

def detail_admin():
    admin.name=input("Enter your name: ")
    admin.adminid=input("Enter the Admin ID: ")
    return

def check():
    if admin.adminid=='1234'or '5678' or '9012' or '3456':
        func()
    else:
        print("Invalid admin ID")

def dets():
    user.name=input("please enter name: ")
    user.group=input("Please enter blood group: ")
    user.area=input("Please enter area number: ")
    user.cont=input("Please enter contact number: ")


def func():
    f=input("View details or Add details or Send request? [v/a/r]")
    if f=='v':
        file=open('donors.txt','r')
        for line in file:
            print(line)
        file.close()
    elif f=='a':
        dets()
        don()
    elif f=='r':
        dets()
        request()

def adm():
    detail_admin()
    check()

s=input("Are you a user or an administrator?[u/a]")
if s == 'u':
    use()
elif s == 'a':
    adm()
else:
    print("Wrong choice")