#while
'''i=0
while i<=10:
    i+=1
    print(i)
    i+=1'''
'''i=100
while i>=0:
    print(i)
    i-=1'''
'''n=int(input())
i=1
while i<=10:
    print(n,"*",i,"=",n*i)
    i+=1'''
'''n=int(input())
i=10
while i>=1:
    print(n,"*",i,"=",n*i)
    i-=1'''
#list using while loop
'''x=[1,2,3,5,4]
i=0
while i<len(x):
    print(x[i])
    i+=1'''
'''x=["a","b","e","c","f"]
i=len(x)-1
while i>=0:
    print(x[i])
    i-=1
else:
    print(True)'''

'''x=["a","b","e","c","f"]
i=0
while i<len(x):
    print(x[0:5:2])
    i+=1'''
'''x=["a","b","e","c","f"]
l=[]
i=0
while i<len(x):
    if i%2==0:
        l.append(x[i])   #l+=x[i]
    i+=1
print(" ".join(l)) #print(l)'''

'''x=["a","b","e","c","f"]
#{0:"a",1:"b",2:"e",3:"c",4:"f"}
d={}
i=0
while i<len(x):
    #print(i)
    #print(x[i])
    d[x[i]]=i   #d[i]=x[i]
    i+=1
print(d)'''

#dictionary used in for loop
'''x=["a","b","e","c","f"]
d={}
for i in range(len(x)):
    d[i]=x[i]
    #d[x[i]]=i
print(d)'''

'''x = ["a", "b", "e", "c", "f"]
d = {}
i = 0
while i < len(x):
    if i % 2 != 0:
        d[x[i]] = i
    i += 1
print(d)

#using for loop
keys=[]
values= []
for k, v in d.items():
    if v % 2 != 0:
        keys.append(k)
        values.append(v)
print(keys,values)
di={}
for i in range(len(k)):
    di[values[i]]=keys[i]
print(di)'''
     
'''while True:
    n=int(input("enter a values:"))
    if n==1:
        print("run")
    elif n==0:
        break'''

'''balance = int(input("Enter balance: "))
choice = int(input("Enter your choice: "))
i = 0
while i <= 0:
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
    else:
        print("Invalid choice")
    print("Thank you visit again")
    i += 1
        
password = "Nikitha@23"
attempts = 0
while attempts < 3:
    user = input("Enter password: ")
    if user == password:
        print("Login successful")
        break
    else:
        print("Wrong password")
        attempts += 1
if attempts == 3:
    print("Account locked")'''

p=input()
while len(p)==0:
    print("password is empty")
    p=input("enter a password again")
    if p.isalpha():
        print("Invalid password")
    elif p.isdigit():
        print("Invalid password")
    else:
        print("Strong password")


        