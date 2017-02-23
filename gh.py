alist=[]
def bubbleSort(alist,count):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(0,passnum):
            count=count+1
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist,0)
print(alist)
print (count)
