import math

num=int(input('What is the maximal number? '))
for i in range(1, num+1):
    for j in range (1, num+1):
        num2=(i)**2 +(j)**2
        result=num2%num2**0.5
        if  result==0 and num2<=num:
            print (i,j, math.sqrt(num2))

            
