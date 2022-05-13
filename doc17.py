# Write a function for checking the speed of drivers. This function should have one parameter: speed.



def func(n):
    i=1
    while i<=n:
        if i%2==0:
            print(i,"EVEN")
        else:
            print(i,"ODD")
        i=i+1
n=int(input("enter :-"))
func(n)





