n=int(input('enter the number of students : '))
noOfTeachers= n/2
count=0
cost=0
minCost=11*(n)
while ((noOfTeachers)>=n/10):
    cost=(noOfTeachers*12)+(n*5)
    if(cost<minCost):
        minCost=cost
    else:
        noOfTeachers-=1
        count+=1

print('total no of ways to go for the play = '+str(count))
print('minimum cost to go for the play = '+str(cost))
