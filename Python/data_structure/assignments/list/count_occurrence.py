list=[12,32,65,45,98,32,78]
count=0
f=int(input('enter a repeated integer'))
for i in list:
    if i == f:
        count +=1
print(count)