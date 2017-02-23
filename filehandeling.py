file=open('f.txt','w')
file.write('My favorite subject is ICT\n')
file.write('My school is located in the western province\n')
file.write('My parents are providing expenses for my education\n')
file.close()

file1=open('f.txt','a')
file1.write('Sri Lanka is one of the beautiful country in the world\n')
file1.close()

file2=open('f.txt')
str1=file2.readline()
str2=file2.readline()
str3=file2.readline()
str4=file2.readline()
print(str1, str2, str3, str4)
file2.close()

file3=open('f.txt')
for line in file3:
    print(line)
file3.close()
