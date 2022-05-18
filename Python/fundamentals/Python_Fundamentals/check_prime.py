a=int(input())
if a>1:
    for x in range(2,int((a/2)+1)):
        if((a%x)==0):
            print("Not a Prime")
            break
        else:
            print('Prime')