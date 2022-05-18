d1={1:10,2:20}
d2={3:30,4:40}
d3={5:50,6:60}
s={}
for i in (d1,d2,d3):
    s.update(i)
print(s)