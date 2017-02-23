file=open('myfile.txt','w')
file.write('1 Sri lanka is beautiful!\n')
file.write('2 Sri lanka is beautiful!\n')
file.write('3 Sri lanka is beautiful!\n')
file.write('4 Sri lanka is beautiful!\n')
file.close()

##file=open('myfile.txt')
##str1=file.readline()
##str2=file.readline()
##print(str1, str2)
##file.close()

##file=open('myfile.txt','r')
##for x in file:
##    print(x)
##print(file.closed)
##print(file.name)
##print(file.mode)
##file.close()

file=open('myfile.txt','a')
file.write('hi hi hi hi')
##s=file.read()
##print(s)
file.close()

##file=open('myfile.txt')
##for x in file:
##    print(x)
##file.close()

file=open('myfile.txt', 'r+')
print(file.read())
position=file.tell()
print(position)
file.seek(110,0)
print(file.read())
file.close()
