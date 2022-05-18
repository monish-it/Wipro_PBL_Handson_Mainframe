s="Hello how aRe YoU"
up=0
lo=0
for i in s:
    if i.isupper():
        up+=1
    else:
        lo+=1
print("Upper case:",up)
print("Lower case:",lo)