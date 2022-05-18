n=int(input())
f=open('text.txt')
for i in range (n):
    print(f.readline())
f.close()