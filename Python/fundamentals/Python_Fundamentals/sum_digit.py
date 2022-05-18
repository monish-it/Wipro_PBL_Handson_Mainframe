a=int(input())
sum = 0
while (a>0):
    d=a%10
    sum+=d
    a=a//10   #floor division
print('sum of digit is :',sum)