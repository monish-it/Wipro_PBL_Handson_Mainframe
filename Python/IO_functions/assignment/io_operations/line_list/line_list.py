f=open('text.txt')
l=[]
for line in f:
    l.append(line)
f.close()
print(l)