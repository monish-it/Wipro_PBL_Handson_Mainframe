try:
    a=int(input())
    for i in range(2,a):
        if(a%i)==0:
            print('Not a Prime')
            break
    else:
        print('Prime number')
except ValueError:
    print('Enter a valid integer')