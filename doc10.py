# Numbers ending with zeros are boring.

# They might be fun in your world, but not here.

# Get rid of them. Only the ending ones.

# 1450 -> 145
# 960000 -> 96
# 1050 -> 105
# -1050 -> -105


# def zero():
#     a=[11000,2000,32000,400,5200]
#     i=0
#     b=[]
#     while i<len(a):
#         while a[i]>0:
#             if a[i]%10!=0:
#                 b.append (a[i])
#                 break
#             a[i]//=10
#         i=i+1
#     print(b)
# zero()

# def num():
#     b=int(input("enter the number"))
#     i=0
#     c=[]
#     while i<len(b):
#         while b[i]>0:
#             if b[i]%10!=0:
#                 c.append(b[i])
#                 break
#             b[i]//10
#         i=i+1
#     print(c)
# num()


a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if a<b and a>c:
    print( a,"second greatest num")
elif b<a and b>c:
    print(b,"second greatest nu")
elif c<a and c>b:
    print(c,"is second greatest n")        

