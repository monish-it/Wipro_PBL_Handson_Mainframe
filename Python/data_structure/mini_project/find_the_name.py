#Find the name
txt=input("sample input : ")
f=input("enter the name to find number of occurrences : ")
c=0
for i in range (len(txt)):
    if (txt[i:i+len(f)])==f:
        c+=1
print(c)