f1=open('Marks.txt')
array_1=[]
##array_2=[]
##for line in f1:
##    array_1.append(line)
##    for a in array_1:
##        str1=line.split()
##        array_2.append(str1)
##print(array_1)
##print(array_2)

for line in f1:
    str1=line.split()
    array_1.append(str1)
length=len(array_1)

for a in range(0, length):
    print(str(array_1[a][0])+' '+ str(len(array_1[a]))+' practical sessions')

print('total no of students is ', length)
f1.close()

f2=open('Marks.txt', 'r+')
f3=open('FinalMarks.txt', 'w')
array_1=[]
sum1=0
for line in f2:
    str1=line.split()
    array_1.append(str1)
length=len(array_1)    
    
for a in range(0, length):
    length2=len(array_1[a])
    if length2==11:
        for b in range(1, 11):
            sum1 = sum1 + int(array_1[a][b])
        average=sum1/10
        f3.write(str(array_1[a][0])+' '+str(sum1)+' '+str(average)+' ')
f2.close()
f3.close()

f4=open('FinalMarks.txt')
str1=f4.read()
print(' read :', str1)
f4.close()

f5=open('Marks.txt','a')
array=[]
for a in (0, 2):
    str1=input('Name: ')
    array.append(str1)
    for b in range(0, 10):
        num=input('marks:')
        array.append(num)
    f5.write(str(array))
f5.close()

f=open('Marks.txt')
str2=f.read()
print(str2)
f.close()



