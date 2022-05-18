list1=[12,32,65,45,98]
list2=[1,3,6,5,8]
for i in range (len(list1)):
    list2.insert(0,list1[-i-1])
print(list2)