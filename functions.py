#positional argument
'''def student(name,age,marks):
    print(name,age,marks)
student("Nikitha",20,75)'''

#keyword argument
'''def student(name,age,marks):
    print(name,age,marks)
student(name="Nikitha",marks="75",age="20")'''

#default argument
'''def student(name,age,marks,institue="a"):
    print(name,age,marks,institue)
student("Nikitha",75,20,"B")'''

#eligible for scholarship
'''def details(name,age,marks,institue="codegnan"):
    if age>20 and marks>=450:
        print("Eligible for scholarship")
    else:
        print("Not eligible for scholarship")
details("Chintu",21,500,"codegnan")'''

#calculate (variable length keyword)
'''def Calculator(x,y,z=0,a=0):
    print(x+y+z)'''
'''def Cal(*values):
    count=0
    print(sum(values))
    print(*values)
    for v in values:
        count+=v
    print(count)
# Calculator(10,20,40)
# Calculator(1,2)
# Calculator(1,2,3,4)
if __name__=="__main__":
    Cal(10,20,30,40,50,60)'''
#restaurant
'''def restaurant(table,*items,count=0):
    print(len(items))
    print(table)
    print(items)
if __name__=="__main__":
    restaurant(12,"biryani","curry","prawns")'''

#keyword varaible length
'''def order(**items):
    count=0
    print(len(items))
    print(items)
order(snack="burger",toppings=2,cheese=1,sauce=3,drinks=4)'''

'''def report(**args):
    print(args)
report(h10=1.23,h11=23.22,h12=0.0,h14=34.90)'''

'''def report(**args):
    print(args)
    if args[bp]>=80 or args[hameglobin]==12.0:
        print("No problems")
    else:
        print("problem")
bp=int(input())
hameglobin=int(input())
report(bp,hameglobin)'''

'''x=20  #global
def Local(a,b):
    print(a,b)         #local
    global x           #it changes both local and global
    x=50
    print(x)
Local(10,20)
print(x)'''
#local variable assign
'''x=20
def local(a,b):
    print(a,b)
local(10,20)
print(x)'''

balance = int(input("Enter balance: "))
def check_balance():
    print("Available balance:", balance)
def withdraw():
    global balance
    amount = int(input("Enter withdraw amount: "))
    if amount <= balance:
        balance -= amount
        print("Transaction successful")
        print("Withdraw amount:", amount)
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance")
def deposit():
    global balance
    amount = int(input("Enter deposit amount: "))
    balance += amount
    print("Deposit successful")
    print("Current balance:", balance)
def atm():
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            check_balance()
        elif choice == 2:
            withdraw()
        elif choice == 3:
            deposit()
        elif choice == 4:
            print("Thank you, visit again!")
            break
        else:
            print("Invalid choice")
atm()