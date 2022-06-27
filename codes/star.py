# increasing down star
i = 0
while i<=5:
    j=0
    while j<=i:
        print('*',end=" ")
        j=j+1
    print()
    i=i+1

print()

# decreasing down star
i = 0
while i<=4:
    j=4
    while j>=i:
        print('*',end=" ")
        j=j-1
    print()     
    i=i+1

#Pyramid
num = int(input("enter rows:"))
i = 0
k = 0
for i in range(num):
    j = 0
    while j<=3-i:
        print('_',end=" ")
        j+=1
    s = 0
    while s <= k:
        print("*",end=" ")
        s+=1    
    k+=2
    print()
i+=1

