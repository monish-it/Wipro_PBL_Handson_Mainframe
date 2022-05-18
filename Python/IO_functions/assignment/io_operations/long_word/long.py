f=open('text.txt','r')
s=f.read()
word=s.split()
maxlen=len(max(word,key=len))
for w in word:
    if len(w)==maxlen:
        longest=w
print(longest)
f.close()