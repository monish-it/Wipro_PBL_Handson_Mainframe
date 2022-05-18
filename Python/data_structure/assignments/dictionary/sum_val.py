from winreg import DeleteValue


d={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 8: 60}
sum=0
for i in d:
    sum = sum + d[i]
print(sum)