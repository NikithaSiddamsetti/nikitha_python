#direct iterable
'''x=[10,21,41,50,77]
for i in x:
    if i%2!=0: 
        print(i)
    else:
        print("even")
    
x=int(input())
for i in x:
    if i%2==0:
        print("even")
    else:
        print("odd")'''
'''x="srujana"
for i in x:
    print(i.upper())'''

'''y="sr5uja123456n0a"
letters = ""
numbers = ""
count=0
for i in y:
    if i.isdigit():
        numbers+=i #n=n+i
        count+=int(i)
    elif i.isalpha():
        letters+=i
print("Letters:",letters)
print("Numbers:",numbers)
print(count)'''

'''z={"a":100,"b":200,"c":300}
for k,v in z.items():
    if v>150:
        print(k)
    else:
        print(v)'''

'''x=[1,2,3,4]
y=["a","b","c","d"]
d={}
for i in range(1,5):'''
#negative
'''for i in range(-10,-30,-3):
    print(i)'''

'''x=[1,2,3,4,5,6,7,8,9]
largest=x[0]
for i in x:
    if i%2==0:
        if x[i]%2!=0:
            print(x[i])
    if i>largest:
        largest=i
print(largest)'''
        
'''for i in range(1,20,1):
    print(i)
else:
    print("completed")'''
n=int(input())
for i in range(n):
    if i==30000:
        break
    print(i)
