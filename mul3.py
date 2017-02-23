def mul3(n):
    if n==1:
        return 3
    else:
        return 3+mul3(n-1)
for i in range(1,10):
    print(mul3(i), end=',')

