def fun(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return n+fun(n-1)

print(fun(5))
