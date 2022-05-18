from black import out


s=input('enter the string ')
if len(s)>=2:
    output= (s[0]+s[1])*len(s)
    print(output)
else:
    print("string lenght is not valid")