def colorsort(s):
    word=s.split('-')
    word.sort()
    print('-'.join(word))
    
a=input()
colorsort(a)