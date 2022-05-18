from black import out


l=[(10,20,40),(50,60,70),(80,90,11)]
for i in l:
    out=[i[:-1]+(100,)]
    print(out,end="")