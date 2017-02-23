f = open("TimeSheet.txt","r")
timeLines = f.readlines()

for time in timeLines:
    tList = time.split()
    print(tList)
    if len(tList)>7:
        print(tList[0],"-",len(tList)-1,"practice sessions")
f.close()
