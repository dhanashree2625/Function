# Q6.Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8].


def a():
    b=[1,2,3,4,5,6,7,8,9]
    i=0
    c=[]
    while i<len(b):
        if b[i]%2==0:
            c.append(b[i])
        i=i+1
    print(c)
a()
