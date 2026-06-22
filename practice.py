'''a,b,c=map(int,input().split())
largest=a
if b>largest:
    largest=b
if c>largest:
    largest=c
print(largest)'''

"""n=int(input())
if n==0:
    print("Zero")
elif n>0:
    print("Positive")
else:
    print("Negative")
"""
'''age=int(input())
if age<=12:
    print("Child")
elif age<=19:
    print("Teenage")
else:
    print("adult")'''
"""marks=int(input())
if marks>=90:
    print("A")
elif marks>=80:
    print("B")
elif marks>=70:
    print("C")
elif marks>=60:
    print("D")
elif marks>=50:
    print("E")
else:
    print("F")"""

"""age=int(input())
salary=int(input())
if age>=20:
    if salary>=20000:
        print("Eligible for loan")"""

'''student_marks=int(input())
if student_marks>90:
    print("get a scholarship")
if student_marks>35:
    print("pass")
else:
    print("Fail")'''
'''a=["Monday","tuesday","Wednesday","Thursday","Friday"]
b=["Saturday","Sunday"]
week_days=input().lower()
weekend_days=input().lower()
if week_days in a:
    print("Working day")
else:
    print("Weekend")'''

"""amount=int(input("Enter a purchase amount:"))
if amount>=10000:
    print("You got 20% discount")
elif amount>=5000:
    print("You got 15% discount")
elif amount>=3500:
    print("you got 10% discount")
elif amount>=1000:
    print("you got 5% discount")
else:
    print("No discount is available")"""

balance = int(input())
choice = int(input("Enter your choice: "))
if choice == 1:
    print("Check Balance")
    print("Available balance:", balance)
elif choice == 2:
    print("Withdraw")
    amount = int(input("Enter withdraw amount: "))
    if amount <= balance:
        balance = balance - amount
        print("Transaction successful")
        print("Withdraw amount:", amount)
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance")
elif choice == 3:
    print("Deposit")
    deposit = int(input("Enter deposit amount: "))
    balance = balance + deposit
    print("Deposit successful")
    print("Current balance:", balance)
    print("Thank you visit again")
else:
    print("Invalid choice")
'''
a=int(input())
b=int(input())
c=int(input())
if a>b:
    if a!=b:
        print("a")
        if a>b and b>c:
            print("b")
            if b>c==a:
                print("successfull")
            elif a>b or a>c:
                print("a")
            elif a!=c and b!=c:
                print("solve")
            elif a>0 or b<0:
                print("True")
            else:
                print("Not successfull")
        else:
            print("None")
    else:
        print("Incorrect numbers:")
else:
    print("completed")
'''







