#Find the runner up
list=[]
n=int(input('Enter total number of participants'))
for i in range(n):
    x=int(input())
    list.append(x)
winner=max(list)
list.remove(winner)
runner=max(list)
print(runner)