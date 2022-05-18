a=int(input())
b=a
rev=0
while (a>0):
    d=a%10
    rev=(rev*10)+d
    a=a//10
if (rev==b):
    print('Palindrome')
else:
    print('Non Palindrome')