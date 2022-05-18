def factorial(n):
    f=1
    if n<0:
        print('Enter positive integer')
    elif n==0:
        print('Enter positive integer')
    else:
        for i in range(1,n+1):
            f=f*i
        return f
print(factorial(5))