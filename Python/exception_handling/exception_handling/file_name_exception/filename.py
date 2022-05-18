a=input()
try:
    file=open(a,'r')
    print(file.read())
except FileNotFoundError:
    print('Enter a valid file name')