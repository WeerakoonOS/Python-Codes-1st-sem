def interest(years):
    A1=(1+(8/1200))
    amount=(A1**(12*years))*10000
    return amount

noOfYears=int(input('Enter no of years to which amount is compounded for :'))
a=interest(noOfYears)

print(a)
