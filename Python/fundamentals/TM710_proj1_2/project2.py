#Ride on mile 1
charge=float(0.51)
d=float(charge*24)
w=float(d*7)
m=float(w*4)  #assuming 28 days in a month
c=918/d
print('It costs '+str(d)+'$ per day')
print('It costs '+str(w)+'$ per week')
print('It costs '+str(m)+'$ per month')
print('At the cost of $918 The server can operate for ' +str(c)+' days')