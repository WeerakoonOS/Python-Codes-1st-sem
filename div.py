dlist=[]
for i in range (0,10):
    num1=int(input('Enter number :'))
    for num in range(1,num1+1):
        if num1%num==0:
            if num not in dlist: 
                dlist.append(num)
dlist.sort()  
print(dlist)
