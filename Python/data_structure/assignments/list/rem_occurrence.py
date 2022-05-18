list=[12,32,65,45,98,32,45,32,96]
f=int(input('enter a integer'))
for i in list:
    if f==i:
        list.remove(i)
        break
print(list)