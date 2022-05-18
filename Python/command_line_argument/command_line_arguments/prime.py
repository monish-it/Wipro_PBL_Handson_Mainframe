from sys import argv
sum=0
for j in range (1,len(argv)):
    num=int(argv[j])
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            break
    else:
        sum=sum+num           
print(sum)