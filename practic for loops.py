'''n=int(input("enter no's:"))
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)'''
#factorial
'''n=int(input())
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)'''
#count
'''n=int(input())
count=0
for i in range(1,n+1):
    count+=1
    print(count)'''
#squares
'''n=int(input())
for i in range(1,n+1):
    a=i*i
    print(a)'''
#cubes
'''n=int(input())
for i in range(1,n+1):
    a=i*i*i
    print(a)'''
#largest
'''a=[10,30,50,80,100]
largest=a[0]
for i in a:
    if i>largest:
        largest=i
print(largest)'''
#smallest
'''a=[10,20,5,8]
smallest=a[0]
for i in a:
    if i<smallest:
        smallest=i
print(smallest)'''
#reverse
'''n=input()
for i in range(len(n)-1,-1, -1):
    print(n[i])'''
#count of even and odd
'''n=int(input())
count=0
count1=0
for i in range(1,n+1):
    if i%2==0:
        count=count+1
    if i%2!=0:
        count1=count1+1
print(count)
print(count1)'''
#sum of all elements
'''n=int(input())
sum=0
for i in range(0,n+1):
    sum+=i
print(sum)'''
#student marks average and total
'''n=int(input("enter numbers:"))
total=0
average=0
for i in range(n):
    marks=int(input("enter marks:"))
    total+=marks
average=(total/n)
print(average)
print(total)'''
#gorcery bill calculator
'''n=int(input("enter no.of grocery items:"))
total=0
for i in range(n):
    cost=int(input("enter a cost"))
    total+=cost
print(total)'''
#table
'''n=int(input())
for i in range(1,21):
    print(n,"*",i,"=",n*i)'''

'''3. Employee Salary Count
Scenario: A company wants to count how many employees have a salary greater than ₹50,000.
Sample Input:
5
30000
60000
45000    sample  output: 3
70000
55000'''
'''n=int(input("no of employees:"))
count=0
for i in range(n):
    m=int(input("no of salaries:"))
    if m>50000:
        count+=i
print(count)'''
'''for i in range(-2,7,-1):
    print(i)'''
#fibanocci series
'''a=int(input())
b=int(input())
for i in range(0,10):
    print(a)
    c=a+b
    a=b
    b=c'''
'''total=0
for i in range(9,0,-2):
    total+=i
    print(i)
print(total)'''
'''total=0
for i in range(3,16,3):
    total+=i
    print(i)
print(total)'''
'''
a=input()
vowels="aeiou"
count=0
for char in a:
    if char in vowels:
        count+=1
print(count)'''

'''a="#coder1234mava"
result=" "
for i in a:
    if i.isdigit() or i=="#":
        result+=i
print(result)'''
'''for i in a:
    if not(i.isalpha()):
        print(i,end="")'''
'''for i in range(1,101):
    if i==50:
        break
    elif i%5==0:
        continue
    else:
        print(i)
for i in range(1,101):
    if i%5!=0:
        print(i)'''
'''for i in range(1,101):
    #if i==50:
     #   break
    if i%5==0:
        continue
    else:
        print(i)
else:
    print("completed")'''
#table
n=int(input())
for i in range(1,21):
    #print(f"{n}*{i}={n*i})
    print(n,"*",i,"=",n*i)
#reverse table
n=int(input())
for i in range(10,0,-1):
    if i%2==0:
        print(n,"*",i,"=",n*i)