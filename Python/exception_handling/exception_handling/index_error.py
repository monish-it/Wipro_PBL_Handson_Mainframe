a=[22,56,32,78,15,98,54,32,91,54]
i=int(input())
try:
    if(a[i-1]<0):
        print('Negative')
    else:
        print('Positive')
except IndexError:
    print('Enter a number between 1 and 10')