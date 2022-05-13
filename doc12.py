# Q14.Write a function to check if a number is prime or not.


def prime(a):
    i=2
    while i<a:
        if a%i==0:
            print(a,"not prime" )
            break
        i=i+1
    else:
        print(a,"prime")
a=int(input("enter the number : "))
prime(a)
