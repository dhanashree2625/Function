# def max(a):
#     i=0
#     m=0
#     while i<len(a):
#         if a[i]>m:
#             m=a[i]
#         i=i+1
#     print(m)
# a=[3,45,7,34,28,89,2,6]
# max(a)



###SECOND MAX###


def max(a):
    i=0
    m=0
    m1=0
    while i<len(a):
        if a[i]>m:
            m1=m
            m=a[i]
        elif a[i]>m1:
            m1=a[i]
        i=i+1
    print(m1)
max([4,6,7,3])


def max(a):
    i=0
    m=0
    m1=0
    m2=0
    while i<len(a):
        if a[i]>m:
            m2=m1
            m1=m
            m=a[i]
        elif a[i]>m2:
            m2=a[i]

            





