def a():
    b=[1,2,3,3,3,3,4,5]
    i=0
    c=[]
    while i<len(b):
        if b[i] not in c:
            c.append(b[i])
        i=i+1
    print(c)
a()