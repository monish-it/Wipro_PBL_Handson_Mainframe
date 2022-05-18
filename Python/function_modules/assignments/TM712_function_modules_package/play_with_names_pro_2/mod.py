def palindrom(s):
    p=s[::-1]
    if p==s:
        print('Palindrome')
    else:
        print('Non-Palindrom')

def vowels(s):
    v="aAeEiIoOuU"
    c=0
    for i in s:
        for j in v:
            if i==j:
                c=c+1
    print('Vowels : ',c)

def freq(s):
    l={}
    for i in s:
        if i in l:
            l[i] += 1
        else:
            l[i] = 1
    print(l)