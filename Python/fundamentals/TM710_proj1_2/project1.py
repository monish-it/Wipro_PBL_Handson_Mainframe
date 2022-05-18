#Ride on mile 1
dist=int(input('How far would you like to Travel?'))
if dist<1:
    print("Enter valid distance")
elif dist<3:
    print('I suggest By-Cycle to your destination')
elif dist>3 and dist<300:
    print('I suggest Motor-Cycle to your destination')
else:
    print('I suggest Super-Car to your destination')