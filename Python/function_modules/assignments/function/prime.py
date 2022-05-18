def chckprime(num):
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print("Not prime")
            break
    else:
        print("Prime")
a=int(input())
chckprime(a)