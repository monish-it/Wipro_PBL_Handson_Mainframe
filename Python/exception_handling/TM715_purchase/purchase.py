fn=input('Enter the file name : ')
f=open(fn)
word=f.read().split()
d={}
for i in range(0,len(word),2):  #Converting word in file to dictionary as key(product):value(price)
    d[word[i]]=word[i+1]
price=[]
price=list(d.values())  #Creating list with all the price from previously created dictionary
free=0
sum=0
for i in range(len(price)):
    try: 
        sum=sum+int(price[i]) #calculating sum of all price
    except ValueError: #catching exception when value for price is not int (i.e Free)
        sum=sum+0
        free=free+1 #calculating number of free items
pro=list(d.keys()) #Creating list with all the product name from previously created dictionary
for i in range (len(d.keys())):
    if pro[i] =="Discount":
        discount_price=int(price[i]) #Finding discout price
# Printing all the outputs
print('Number of item purchased = '+str(len(price)-1))
print('Number of free items = '+str(free))
print('Amount to pay = '+str(sum))
print('Discount gave = '+str(discount_price))
print('Final amount = '+str(sum-discount_price))
f.close()