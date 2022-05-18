def time(file):
    t=0
    for lines in file:
        t+=1
    if t>12:
        t=t-12
        print('Time: '+str(t)+' pm')
    else:
        print('Time: '+str(t)+' am')

def place(file):
    f=file.read()
    c={}
    word=f.split()
    for w in word:
        if w in c.keys():
            c[w]+=1
        else:
            c[w]=1
    # print(c.items())
    c=sorted(c.items(),key=lambda kv: kv[1])
    a=list(dict(c).keys())
    print('Place : '+a[-1])

ftime=open('sample.txt','r')
fplace=open('sample.txt','r')
time(ftime)
place(fplace)
ftime.close()
fplace.close()