##f2=open('TimeSheet.txt', 'r')
##timeArray=[]
##count=0
##
##for line in f2:
##    timeArray.append(line.split())
##for term in range (0, len(timeArray)):
##    if len(timeArray[term])>=8:
##        count+=1
##print(count)
##f2.close()

##f2=open('TimeSheet.txt', 'r')
##timeArray=[]
##minNum=0
##
##for line in f2:
##    timeArray.append(line.split())
##
##for term in range (0, len(timeArray)):
##        timeArray[term].sort()
##        print(timeArray[term].pop()+' '+timeArray[term][0])
##        
##        
##        if minNum<int(timeArray[term][a]) :
##            minNum=int(timeArray[term][a])
##        else:
##            print(str(timeArray[term][0]), minNum)
#f2.close()

f2=open('TimeSheet.txt')
f3=open('AverageTime.txt','w')
timeArray=[]
sum1=0

for line in f2:
    timeArray.append(line.split())

for term in range(0, len(timeArray)):
    for a in range(1, len(timeArray[term])):
        sum1=sum1+int(timeArray[term][a])
    avg=sum1/len(timeArray[term])
    f3.write(str(timeArray[term][0])+' '+ str(avg))

f2.close()
 
f4=open('AverageTime.txt')
for line in f4:
    array.append(line.split())
    for term in range(0, len(array)):
        if m
f4.close()


    
