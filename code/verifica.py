def func(a):
    if (a >= '' and a <= '/' or a >= ':' or a == None):
        return -1
    else:
        b=eval(a)
        return b