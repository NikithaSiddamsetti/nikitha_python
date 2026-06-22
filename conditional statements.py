#if condition
"""age=int(input())
card=input().lower()
if age>=18 and card=="yes":
    print("eligible")
else:
    print("Not eligible")
"""
"""user="Nikitha"
password="Nikitha@2005"
u=input().title()
p=input().title()
if u==user and p==password:
    print("Login succesfully")
else:
    print("Invalid password")
"""
"""x= ["a","b","c","d"]
user=input().lower()
if user in x:
    print("available")
else:
    print("Not")"""
"""
a,b,c=map(int,input().split())
if a < b and a <c:
    print(a)
elif b <a and b <c:
    print(b)
else:
    print(c)"""

"""n=int(input())
if n%3==0 and n%5==0:
    print("Fizz Buzz")
elif  n%3==0:
    print("Fizz ")
else:
    print("Buzz")"""

"""name=input("name:").lower()
marks=int(input("marks:"))
if marks>=90:
    print(f"name:{name},marks:{marks},Grade:A")
elif marks>=80:
    print(f"name:{name},marks:{marks},Grade:B")
elif marks>=70:
    print(f"name:{name},marks:{marks},Grade:C")
elif marks>=60:
    print(f"name:{name},marks:{marks},Grade:D")
elif marks>=50:
    print(f"name:{name},marks:{marks},Grade:E")
else:
    print(f"name:{name},marks:{marks},Grade:Fail")"""

"""name = input("Name: ")
marks = int(input("Marks: "))
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
elif marks >= 50:
    grade = "E"
else:
    grade = "Fail"
print(f"name:{name}\n marks:{marks}\n Grade:", grade)"""

"""name = input("Name: ").lower()
grade= input("grade: ").lower()
if grade  =="A":
    seat_allocated = "Free"
elif grade == "B":
    seat_allocated = "20%"
elif grade == "C":
    seat_allocated = "15%"
elif  grade=="D":
    seat_allocated = "10%"
else:
    print("50000")
print(f"name:{name}\n grade:{grade}\n seat_allocated:", seat_allocated)"""
'''name = input("Name: ").lower()
grade= input("grade: ").lower()
price=50000
if grade=="A":
    print("free")
if grade  =="B":
    discount=20/100
elif grade=="C":
    discount=15/100
elif grade=="D":
    discount=10/100
else:
    amount=price
amount=price-(price*discount)'''


'''a,b,c=map(int,input().split())
largest=a
if  b>largest:
    largest=b
if  c>largest:
    largest=c
print(largest)'''

'''user=["Nikitha","abc","xyz","cdg"]
p=12345
username=input()
if username in user:
    password=int(input("Enter password:"))
    if password==p:
        print("login success")
    else:
        print("wrong password")
else:
    print("wrong credentials")'''

'''person=input()
if person=="yes":
    college=input("Are you in college:")
    if college=="yes":
        floor=input("Are you see in floor:")
        if floor=="yes":
            blockprint("Are you see in block:")
            if 
        else:
            print("No")
    else:
        print("No")
else:
    print("Not in college")'''

'''college = input()
if college == "yes":
    block = input()
    if block == "yes":
        floor = input()
        if floor == "yes":
            classroom = input()
            if classroom == "yes":
                print("classroom")
            else:
                print("floor")
        else:
            print("block")
    else:
        print("college")
else:
    print("absent")
'''

'''year=int(input())
if year%4==0 and year%100!=0 or year%400==0:
    print("Leap year")
else:
    print("Not leap year")'''
    
choice=int(input("enter your choice:"))
if choice==1:
    print("Bike")
    km=int(input())
    if km in range(1,9):
        price=km*5
        print("Total price:",price)
    elif km in range(9,16):
        price=(km-8)*6+40
        print("Total price:",price)
    elif km in range(16,26):
        price=(km-15)*8+76
        print("Total price:",price)
    elif km in range(26,31):
        price=(km-25)*10+188
        print("Total price:",price)
    else:
        print("No ride available")
        price = 0
if choice==2:
    print("Auto")
    km=int(input())
    if km in range(1,11):
        price=km*8   #1–10 km → 10 × 8 = ₹80
        print("Total price:",price)
    elif km in range(11,20):
        price=(km-10)*10+80  #11–19 km → 9 × 10 = ₹90
        print("Total price:",price)
    elif km in range(20,36):
        price=(km-19)*12+170   #20–35 km → 16 × 12 = ₹192
        print("Total price:",price)
    elif km in range(36,61):
        price=(km-35)*15+350   #36–40 km → 5 × 15 = ₹75
        print("Total price:",price)
    else:
        print("No ride available")
if choice==3:
    print("Car")
    km=int(input())
    if km in range(1,51):
        price=km*12
        print("Total price:",price)
    elif km in range(51,81):
        price=(km-80)*15+588
        print("Total price:",price)
    elif km in range(81,121):
        toll=int(input("enter toll amount:"))
        price=(km-120)*17+1023+toll
        print("Total price:",price)
    elif km in range(121,201):
        toll=int(input("enter toll amount:"))
        food=int(input("enter food bill:"))
        price=(km-200)*18+food+1686+toll
        print("Total price:",price)
    else:
        print("No ride is available")
    

    
    
























