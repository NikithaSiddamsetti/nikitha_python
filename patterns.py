'''for i in range(3):
    for j in range(4,0,-1):
        print(j,end=" ")
    print()
for i in range(4,-1,-2):
    for j in range(3):
        print(i,end=' ')'''
'''for i in range(4,0,-):
    for j in range(i):
        print("*",end=" ")
    print()'''
n=5
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-3 or j==n-1:  #j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

