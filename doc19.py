# Write a function that prints all the prime numbers between 0 and limit where limit is a parameter.


# def func(n):
#     i=1
#     while i<=n:
#         if i%2!=0:
#             print(i,"Prime no.")
#         else:
#             print(i,"not prime")
#         i=i+1
# n=int(input("enter number : "))
# func()


def num():
    i=0
    l=[]
    while i<=n:
        count=0
        j=1
        while j<=i:
            if i%j==0:
                count+=1
            j=j+1
        if count==2:
            l.append(i)
        i=i+1
    print(l)
n=int(input("enter number : "))
num()