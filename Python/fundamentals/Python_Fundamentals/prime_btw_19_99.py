for i in range(10, 99+1):
    for j in range(2, int(i/2)+1):
        if i % j == 0:
            break
    else:
        print(i)    