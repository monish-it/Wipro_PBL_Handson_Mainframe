a=input()
c=0
f=open('text.txt')
s=f.read()
word=s.split()
for w in word:
    if w==a:
        c=c+1
print(c)
f.close