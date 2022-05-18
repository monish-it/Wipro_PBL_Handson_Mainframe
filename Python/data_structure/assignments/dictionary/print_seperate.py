d={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 8: 60}
print('Keys:')
for i in d:
    print(i, end='')
print('\nvalues:')
for i in d:
    print(d[i],end='')
print('\nKey and Value:')
for i in d:
    print(i,d[i])