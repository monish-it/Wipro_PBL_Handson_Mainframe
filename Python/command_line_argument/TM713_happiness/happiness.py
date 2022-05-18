from sys import argv
s1,s2,s3=argv[1].split('-'),argv[2].split('-'),argv[3].split('-')
h=0
for i in s3:
    for j in s1:
        if i==j:    
            h=h+1
    for k in s2:
        if i==k:
            h=h-1
print(h)