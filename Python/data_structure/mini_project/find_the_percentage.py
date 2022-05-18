#Find the percentage
dict={'monish':[54,65,98],'mugesh':[62,98,65],'harish':[65,32,48]}
name=input('Enter the name ')
s=sum(dict[name])
ave=s/len(dict[name])
print('marks for '+name+' are '+str(dict[name])+' and average is '+str(ave))