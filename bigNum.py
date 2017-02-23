count=0
sum1=0
x=0
for i in range(15,500):
    if i%15==0:
        count+=1
remainder=500-(15*count)
val=2**remainder
print(val)
sum1=sum(int(digit) for digit in str(val))
finalCount=count*26

print (finalCount+sum1)
