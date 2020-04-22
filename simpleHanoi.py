def hanoi(n,f,h,t):
    if n != 0:
        hanoi(n-1,f,t,h)
        print("Move disc from {} to {}".format(f,t))
        #move(f,t)
        hanoi(n-1,h,f,t)
hanoi(4,'A','B','C')