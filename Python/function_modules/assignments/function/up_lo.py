def count(s):
    l=u=0
    for i in s:
        if i.isupper():
            u=u+1
        else:
            l=l+1
    print('Uppercase : ',u)
    print('Uppercase : ',l)
s="HellO WorLd"
count(s)