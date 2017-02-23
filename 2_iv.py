##data=[
##    [1,2,3,4],
##    [5,6,7,8],
##    [9,10,11,12],
##    ]
##changed=[]
##lists=[]
##for i in range(4):
##    changed.append([row[i] for row in data])
##print(changed)

######for i in range(4):
######    for row in data:
######        changed.append([row[i]])
######
######print(changed)
##


def changeme( mylist ):
    mylist.append([1,2,3,4]);
    #print ("Values inside the function: ", mylist)

mylist = [10,20,30];
changeme( mylist );
print ("Values outside the function: ", mylist)
