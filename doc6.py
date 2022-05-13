# Q8.Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. Go to the editor
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Uppercase characters : 3
# No. of Lower case Characters : 12



# def a(b=input("enter words : ")):
#     count=0
#     count1=0
#     i=0
#     while i<len(b):
#         if b[i]>="A" and b[i]<="Z":
#            count+=1
#         else:
#            count1+=1
#         i=i+1
#     print("no of upper case",count)
#     print("No of lower case",count1)
# a()
        


def a(b=input("enter the word : ")):
    count=0
    count1=0
    i=0
    while i<len(b):
        if b[i]>="A" and b[i]<="Z":
            count+=1
        else:
            count1+=1
        i=i+1
    print("no of upper case",count)
    print("no of lower case",count1)
a()
